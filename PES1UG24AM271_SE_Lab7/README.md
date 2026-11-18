# SE Lab 7 — Fuzz Testing for Input Validation Bugs

**Student:** Shruti Choudhary  
**SRN:** PES1UG24AM271

## Source
Lab 7 (Weather Alert Classifier) from the assigned `L6_L7_32_weather_alert-main` ZIP. The Lab 7 project uses `weather_alert.py` and `test_weather_alert.py` in place of the handout's generic filenames.

## Run
```bash
python -m pip install pytest hypothesis
python weather_alert.py
python deterministic_regression_checks.py
python -m pytest -v test_weather_alert.py
```

## Validations
- `parse_reading`: finite temperature and humidity integer 0–100 separated by `/`.
- `wind_category`: non-negative integer speed, with none/advisory/warning cutoffs 39 and 89 km/h.
- `rainfall_spread`: finite, non-negative, nonempty CSV readings.

Malformed inputs raise `ValueError`; Hypothesis tests generate arbitrary text and None along with valid values and boundaries.

The report records reproduced failures, fixed application output, passing deterministic regression checks and a blocked pytest/Hypothesis run due to missing Hypothesis dependency in the authoring environment. Run the pytest suite locally after installing Hypothesis to obtain a confirmed passing screenshot.
