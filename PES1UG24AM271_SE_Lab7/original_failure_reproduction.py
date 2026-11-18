"""Reproduce the original failures by providing the original module path."""
import importlib.util
from pathlib import Path
import sys
if len(sys.argv) != 2:
    print('Usage: python original_failure_reproduction.py /path/to/original/weather_alert.py')
    raise SystemExit(2)
spec = importlib.util.spec_from_file_location('original_weather_alert', Path(sys.argv[1]))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
for name in ('parse_reading', 'wind_category', 'rainfall_spread'):
    try:
        getattr(module, name)(None)
    except Exception as exc:
        print(f'{name}(None) -> {type(exc).__name__}: {exc}')
