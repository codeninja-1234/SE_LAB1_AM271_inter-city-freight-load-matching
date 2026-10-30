import pytest
from weather_alert import wind_alert, rain_alert, heat_alert, overall_alert

# Wind: exercise each threshold decision as True and False.
@pytest.mark.parametrize(("speed", "expected"), [
    (89, "warning"), (88, "watch"), (62, "watch"),
    (61, "advisory"), (39, "advisory"), (38, "none"),
])
def test_wind_alert_branches(speed, expected):
    assert wind_alert(speed) == expected

# Rain: exercise both outer decisions and both soil-saturation decisions.
@pytest.mark.parametrize(("rain", "saturated", "expected"), [
    (50, True, "warning"),
    (50, False, "watch"),
    (10, True, "watch"),
    (10, False, "advisory"),
    (9, True, "none"),
])
def test_rain_alert_branches(rain, saturated, expected):
    assert rain_alert(rain, saturated) == expected

# Heat: exercise humidity adjustment and all three index thresholds.
@pytest.mark.parametrize(("temp", "humidity", "expected"), [
    (45, 40, "warning"),  # index >= 45
    (44, 50, "warning"),  # humidity adjustment crosses 45
    (40, 40, "watch"),    # index >= 40
    (35, 40, "advisory"), # index >= 35
    (34, 40, "none"),
    (33, 50, "none"),     # humidity adjustment, but below 35
])
def test_heat_alert_branches(temp, humidity, expected):
    assert heat_alert(temp, humidity) == expected

# Overall: empty/non-empty iteration, valid/invalid alerts, and
# both outcomes of the severity comparison.
def test_overall_alert_branches():
    assert overall_alert([]) == "none"
    assert overall_alert(["none"]) == "none"
    assert overall_alert(["advisory", "watch", "warning"]) == "warning"
    assert overall_alert(["warning", "watch"]) == "warning"
    with pytest.raises(ValueError, match="unknown alert"):
        overall_alert(["storm"])
