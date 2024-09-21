import pytest
from peak import calculate_peak_and_nonpeak_hours

@pytest.mark.parametrize(
    "year, month, expected_peak, expected_non_peak", [
    (2023, 2, 280, 392),
    (2024, 2, 294, 402),
    (2024, 9, 294, 426),
    (2024, 10, 322, 422)
])
def test_calculate_peak_and_nonpeak_hours(year, month, expected_peak, expected_non_peak):
    assert expected_peak, expected_non_peak == calculate_peak_and_nonpeak_hours(year, month)

