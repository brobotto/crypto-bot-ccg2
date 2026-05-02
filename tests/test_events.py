import json
from datetime import UTC, datetime

from cbot.engine.events import (
    Event,
    JsonlEventWriter,
    create_run_directory,
    format_timestamp,
    make_run_id,
    write_json,
)


SCHEMA_DIR = "logs/schema/v1"


def load_schema(name, root):
    return json.loads((root / SCHEMA_DIR / name).read_text(encoding="utf-8"))


def validate_event(record, schema_name, root):
    schema = load_schema(schema_name, root)
    assert set(schema["required"]) <= set(record)
    assert record["schema_version"] == "1.0"
    expected_event_type = schema["properties"]["event_type"].get("const")
    if expected_event_type:
        assert record["event_type"] == expected_event_type
    for key in schema["properties"]["payload"].get("required", []):
        assert key in record["payload"]


def test_make_run_id_is_stable_and_slugged():
    now = datetime(2026, 5, 2, 12, 30, 5, tzinfo=UTC)
    assert make_run_id("SMA Cross Smoke", now) == "run_20260502_123005_sma_cross_smoke"


def test_format_timestamp_outputs_utc_z():
    value = datetime(2026, 5, 2, 12, 30, 5, tzinfo=UTC)
    assert format_timestamp(value) == "2026-05-02T12:30:05Z"


def test_event_matches_envelope_schema(tmp_path):
    root = tmp_path
    schema_root = root / "logs/schema/v1"
    schema_root.mkdir(parents=True)
    source = json.loads(open("logs/schema/v1/event-envelope.schema.json", encoding="utf-8").read())
    (schema_root / "event-envelope.schema.json").write_text(json.dumps(source), encoding="utf-8")

    event = Event(
        event_type="run.started",
        run_id="run_20260502_123005_sma_cross",
        sequence=1,
        payload={},
        timestamp=datetime(2026, 5, 2, 12, 30, 5, tzinfo=UTC),
    )

    validate_event(event.to_record(), "event-envelope.schema.json", root)


def test_writer_appends_sequenced_events(tmp_path):
    path = tmp_path / "events.jsonl"
    writer = JsonlEventWriter(path)

    first = writer.write("run.started", "run_20260502_123005_sma_cross", {"label": "smoke"})
    second = writer.write("run.completed", "run_20260502_123005_sma_cross", {"status": "COMPLETED"})

    assert first.sequence == 1
    assert second.sequence == 2
    records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
    assert [record["sequence"] for record in records] == [1, 2]


def test_create_run_directory_and_write_json(tmp_path):
    now = datetime(2026, 5, 2, 12, 30, 5, tzinfo=UTC)
    run_dir = create_run_directory(tmp_path, "smoke", now)

    write_json(run_dir.config_path, {"ok": True})

    assert run_dir.path.is_dir()
    assert run_dir.config_path.exists()
    assert json.loads(run_dir.config_path.read_text(encoding="utf-8")) == {"ok": True}


def test_core_event_schemas_accept_minimal_valid_records():
    root = __import__("pathlib").Path.cwd()
    run_id = "run_20260502_123005_sma_cross"
    timestamp = "2026-05-02T12:30:05Z"

    records = [
        (
            "run.started.schema.json",
            {
                "schema_version": "1.0",
                "event_type": "run.started",
                "run_id": run_id,
                "timestamp": timestamp,
                "sequence": 1,
                "payload": {
                    "label": "smoke",
                    "sample_label": "IN_SAMPLE",
                    "market": {},
                    "strategy": {},
                    "simulation": {},
                },
            },
        ),
        (
            "strategy.signal.schema.json",
            {
                "schema_version": "1.0",
                "event_type": "strategy.signal",
                "run_id": run_id,
                "timestamp": timestamp,
                "sequence": 2,
                "payload": {
                    "strategy": "sma_cross_v1",
                    "symbol": "BTCUSDT",
                    "timeframe": "1h",
                    "candle_time": timestamp,
                    "signal": "BUY",
                },
            },
        ),
        (
            "simulation.fill.schema.json",
            {
                "schema_version": "1.0",
                "event_type": "simulation.fill",
                "run_id": run_id,
                "timestamp": timestamp,
                "sequence": 3,
                "payload": {
                    "symbol": "BTCUSDT",
                    "side": "BUY",
                    "quantity": 0.1,
                    "price": 50000,
                    "fee": 5,
                    "fee_asset": "USDT",
                    "slippage_bps": 20,
                },
            },
        ),
        (
            "portfolio.snapshot.schema.json",
            {
                "schema_version": "1.0",
                "event_type": "portfolio.snapshot",
                "run_id": run_id,
                "timestamp": timestamp,
                "sequence": 4,
                "payload": {
                    "cash": 4995,
                    "equity": 10000,
                    "drawdown_pct": 0,
                    "positions": {"BTC": 0.1},
                },
            },
        ),
        (
            "run.completed.schema.json",
            {
                "schema_version": "1.0",
                "event_type": "run.completed",
                "run_id": run_id,
                "timestamp": timestamp,
                "sequence": 5,
                "payload": {
                    "status": "COMPLETED",
                    "verdict": "CONDITIONAL",
                    "metrics": {},
                },
            },
        ),
    ]

    for schema_name, record in records:
        validate_event(record, schema_name, root)
