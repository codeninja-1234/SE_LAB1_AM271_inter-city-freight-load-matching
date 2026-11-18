"""Dependency-free regression checks; not a substitute for Hypothesis tests."""
from weather_alert import parse_reading, wind_category, rainfall_spread
assert parse_reading('35.5/80') == (35.5, 80)
for item in ('', None, 'abc', '10/101', 'nan/3', '10/'):
    try:
        parse_reading(item)
    except ValueError:
        continue
    raise AssertionError(f'parse_reading should reject {item!r}')
print('parse_reading valid and invalid cases: PASS')
for speed, expected in [('38','none'),('39','advisory'),('88','advisory'),('89','warning')]:
    assert wind_category(speed) == expected
for item in ('-1', None, 'foo', '2.5'):
    try:
        wind_category(item)
    except ValueError:
        continue
    raise AssertionError(f'wind_category should reject {item!r}')
print('wind_category thresholds 38/39/88/89: PASS')
assert rainfall_spread('2,5.5,10') == 8.0
for item in ('', None, '1,,3', '-1,2', '1,inf'):
    try:
        rainfall_spread(item)
    except ValueError:
        continue
    raise AssertionError(f'rainfall_spread should reject {item!r}')
print('rainfall_spread valid and invalid cases: PASS')
