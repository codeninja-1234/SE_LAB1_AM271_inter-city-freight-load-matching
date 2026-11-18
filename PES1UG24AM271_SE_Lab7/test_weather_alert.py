"""Property-based fuzz tests for the three Lab 7 weather functions."""
import math
import pytest
from hypothesis import given, settings, strategies as st
from weather_alert import parse_reading, wind_category, rainfall_spread

@settings(max_examples=150)
@given(st.text() | st.none())
def test_parse_reading_no_crash(s):
    try:
        result = parse_reading(s)
    except ValueError:
        return
    assert isinstance(result, tuple) and len(result) == 2
    temperature, humidity = result
    assert isinstance(temperature, float) and math.isfinite(temperature)
    assert isinstance(humidity, int) and 0 <= humidity <= 100

@settings(max_examples=150)
@given(st.text() | st.none())
def test_wind_category_no_crash(s):
    try:
        result = wind_category(s)
    except ValueError:
        return
    assert result in {"none", "advisory", "warning"}

@settings(max_examples=150)
@given(st.text() | st.none())
def test_rainfall_spread_no_crash(s):
    try:
        result = rainfall_spread(s)
    except ValueError:
        return
    assert isinstance(result, float)
    assert math.isfinite(result) and result >= 0

@given(st.floats(allow_nan=False, allow_infinity=False, min_value=-1000, max_value=1000), st.integers(min_value=0, max_value=100))
def test_parse_reading_valid(temp, humidity):
    actual_temp, actual_humidity = parse_reading(f"{temp}/{humidity}")
    assert actual_temp == temp
    assert actual_humidity == humidity

@given(st.integers(min_value=0, max_value=500))
def test_wind_category_boundaries(speed):
    expected = "warning" if speed >= 89 else "advisory" if speed >= 39 else "none"
    assert wind_category(str(speed)) == expected

@given(st.lists(st.floats(min_value=0, max_value=1e6, allow_nan=False, allow_infinity=False), min_size=1, max_size=20))
def test_rainfall_spread_valid(values):
    result = rainfall_spread(",".join(map(str, values)))
    assert result == pytest.approx(max(values) - min(values), rel=1e-12, abs=1e-9)

@pytest.mark.parametrize("text", [None, "", "hello", "2/", "/30", "2/101", "2/-1", "nan/50", "inf/50", "2/50/4", 123])
def test_parse_reading_invalid(text):
    with pytest.raises(ValueError):
        parse_reading(text)

@pytest.mark.parametrize("speed", [None, "", "abc", "-1", "2.5", "inf", "nan", True, [], 45.0])
def test_wind_category_invalid(speed):
    with pytest.raises(ValueError):
        wind_category(speed)

@pytest.mark.parametrize("text", [None, "", ",", "1,,3", "abc", "1,nan", "1,inf", "-1,2", "1,", [], 123])
def test_rainfall_spread_invalid(text):
    with pytest.raises(ValueError):
        rainfall_spread(text)
