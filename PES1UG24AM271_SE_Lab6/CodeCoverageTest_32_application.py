import pytest
from weather_alert import wind_alert, rain_alert, heat_alert, overall_alert

def test_wind_alert_levels():
    assert wind_alert(10) == "none"
    assert wind_alert(40) == "advisory"
    assert wind_alert(65) == "watch"
    assert wind_alert(90) == "warning"

def test_rain_alert_levels():
    assert rain_alert(5, False) == "none"
    assert rain_alert(20, False) == "advisory"
    assert rain_alert(20, True) == "watch"
    assert rain_alert(55, False) == "watch"
    assert rain_alert(55, True) == "warning"

def test_heat_alert_levels():
    assert heat_alert(30, 40) == "none"
    assert heat_alert(36, 40) == "advisory"
    assert heat_alert(41, 40) == "watch"
    assert heat_alert(46, 40) == "warning"
    assert heat_alert(44, 50) == "warning"

def test_overall_alert():
    assert overall_alert([]) == "none"
    assert overall_alert(["advisory", "watch"]) == "watch"
    with pytest.raises(ValueError, match="unknown alert"):
        overall_alert(["storm"])
