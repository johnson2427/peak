from src.peak import calculate_peak_and_nonpeak_hours


def test_calculate_peak_and_nonpeak_hours():
    assert 294, 402 == calculate_peak_and_nonpeak_hours(2024, 2)

