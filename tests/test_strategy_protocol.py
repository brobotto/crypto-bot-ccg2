import pytest

from cbot.strategies.protocol import ParameterSpec, StrategyMetadata


def test_strategy_metadata_requires_hypothesis():
    with pytest.raises(ValueError, match="hypothesis"):
        StrategyMetadata(name="x", version="1.0.0", hypothesis="")


def test_strategy_metadata_rejects_negative_warmup():
    with pytest.raises(ValueError, match="warmup"):
        StrategyMetadata(name="x", version="1.0.0", hypothesis="test", warmup_candles=-1)


def test_parameter_spec_holds_bounds():
    spec = ParameterSpec(default=10, description="window", minimum=2, maximum=100)
    assert spec.default == 10
    assert spec.minimum == 2
    assert spec.maximum == 100

