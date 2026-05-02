"""Structured event helpers and append-only JSONL logging."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "1.0"
RUN_ID_PATTERN = re.compile(r"[^a-zA-Z0-9_.-]+")


def utc_now() -> datetime:
    return datetime.now(UTC)


def format_timestamp(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=UTC)
    return value.astimezone(UTC).isoformat().replace("+00:00", "Z")


def slugify(value: str) -> str:
    cleaned = RUN_ID_PATTERN.sub("_", value.strip()).strip("_")
    return cleaned.lower() or "run"


def make_run_id(label: str, now: datetime | None = None) -> str:
    now = now or utc_now()
    stamp = now.astimezone(UTC).strftime("%Y%m%d_%H%M%S")
    return f"run_{stamp}_{slugify(label)}"


@dataclass(frozen=True)
class Event:
    event_type: str
    run_id: str
    sequence: int
    payload: dict[str, Any]
    timestamp: datetime = field(default_factory=utc_now)
    schema_version: str = SCHEMA_VERSION

    def to_record(self) -> dict[str, Any]:
        record = asdict(self)
        record["timestamp"] = format_timestamp(self.timestamp)
        return record

    def to_json(self) -> str:
        return json.dumps(self.to_record(), sort_keys=True, separators=(",", ":"))


class JsonlEventWriter:
    """Append-only writer for one run's structured event stream."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._sequence = 0

    @property
    def next_sequence(self) -> int:
        return self._sequence + 1

    def write(self, event_type: str, run_id: str, payload: dict[str, Any]) -> Event:
        event = Event(
            event_type=event_type,
            run_id=run_id,
            sequence=self.next_sequence,
            payload=payload,
        )
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(event.to_json() + "\n")
        self._sequence = event.sequence
        return event


@dataclass(frozen=True)
class RunDirectory:
    run_id: str
    path: Path

    @property
    def events_path(self) -> Path:
        return self.path / "events.jsonl"

    @property
    def config_path(self) -> Path:
        return self.path / "config.resolved.json"

    @property
    def strategy_meta_path(self) -> Path:
        return self.path / "strategy.meta.json"

    @property
    def report_path(self) -> Path:
        return self.path / "report.json"

    @property
    def summary_path(self) -> Path:
        return self.path / "summary.md"


def create_run_directory(root: Path, label: str, now: datetime | None = None) -> RunDirectory:
    run_id = make_run_id(label, now)
    path = root / run_id
    path.mkdir(parents=True, exist_ok=False)
    return RunDirectory(run_id=run_id, path=path)


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
