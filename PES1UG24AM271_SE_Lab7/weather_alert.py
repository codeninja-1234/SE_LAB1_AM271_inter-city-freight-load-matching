"""Robust weather reading utilities for SE Lab 7 fuzz testing."""
import math

def _finite_number(value, field):
    """Return a finite float for a numeric value, or raise ValueError."""
    if not isinstance(value, (str, int, float)) or isinstance(value, bool):
        raise ValueError(f"{field} must be a finite number")
    try:
        number = float(value)
    except (ValueError, OverflowError, TypeError) as exc:
        raise ValueError(f"{field} must be a finite number") from exc
    if not math.isfinite(number):
        raise ValueError(f"{field} must be a finite number")
    return number

def parse_reading(text):
    """Parse 'temperature/humidity'; humidity must be an integer from 0 to 100."""
    if not isinstance(text, str):
        raise ValueError("reading must be a string in temperature/humidity format")
    parts = text.split('/')
    if len(parts) != 2 or not all(part.strip() for part in parts):
        raise ValueError("reading must contain temperature/humidity")
    temperature = _finite_number(parts[0], "temperature")
    humidity_text = parts[1].strip()
    try:
        humidity = int(humidity_text)
    except (ValueError, OverflowError) as exc:
        raise ValueError("humidity must be an integer from 0 to 100") from exc
    if not 0 <= humidity <= 100:
        raise ValueError("humidity must be an integer from 0 to 100")
    return temperature, humidity

def wind_category(speed_text):
    """Classify non-negative whole-number wind speed (km/h)."""
    if not isinstance(speed_text, (str, int)) or isinstance(speed_text, bool):
        raise ValueError("wind speed must be a non-negative integer")
    try:
        speed = int(speed_text)
    except (ValueError, OverflowError, TypeError) as exc:
        raise ValueError("wind speed must be a non-negative integer") from exc
    if speed < 0:
        raise ValueError("wind speed must be a non-negative integer")
    if speed >= 89:
        return 'warning'
    if speed >= 39:
        return 'advisory'
    return 'none'

def rainfall_spread(readings_csv):
    """Return max-min for non-empty CSV of non-negative, finite rainfall in mm."""
    if not isinstance(readings_csv, str) or not readings_csv.strip():
        raise ValueError("rainfall readings must be non-empty CSV text")
    fields = readings_csv.split(',')
    if any(not field.strip() for field in fields):
        raise ValueError("rainfall entries must not be empty")
    readings = [_finite_number(field, "rainfall") for field in fields]
    if any(value < 0 for value in readings):
        raise ValueError("rainfall must not be negative")
    spread = max(readings) - min(readings)
    if not math.isfinite(spread):
        raise ValueError("rainfall spread is outside supported numeric range")
    return spread

def main():
    demos = [
        ("parse_reading", parse_reading, "35.5/80", "invalid"),
        ("wind_category", wind_category, "45", "-2"),
        ("rainfall_spread", rainfall_spread, "2,5.5,10", "2,,10"),
    ]
    for name, operation, valid, invalid in demos:
        print(f"==== Running {name} ====")
        for sample in (valid, invalid):
            try:
                print(f"Input: {sample!r} -> {operation(sample)!r}")
            except ValueError as exc:
                print(f"Input: {sample!r} -> rejected: {exc}")
        print()

if __name__ == "__main__":
    main()
