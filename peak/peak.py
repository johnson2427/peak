import calendar


def calculate_peak_and_nonpeak_hours(year: int, month: int) -> tuple[int, int]:
    """
    Calculate the Peak and Non-Peak hours of a Month.

    Args:
        year (int): Choose a year in YYYY format.
        month (int): Choose a month in m format. e.g. January = 1

    Returns:
        (int, int): Peak and non-peak hours for a month.
    """

    # Initialize counters
    peak_hours = 0
    non_peak_hours = 0

    # Create a calendar object
    cal = calendar.Calendar()

    # Iterate through all days in the specified month
    for day in cal.itermonthdates(year, month):

        # Note: Calandar.itermonthdates starts on the first Monday of
        #       a week that includes the first day of the month. If
        #       the first day of the month is on a Wednesday, they prior
        #       month's last two days will be included in this check.
        #       Exclude the days that are included from the prior month.
        if day.month != month:
            continue

        # Note: Determine the day of the week (Monday=0, Sunday=6)
        weekday = day.weekday()

        # Note: Peak days are Monday-Friday (0-4)
        if weekday < 5:
            # Note: 6AM-8PM == 14 hours
            peak_hours += 14
            non_peak_hours += 10
        else:
            # Note: Weekends are not peak hours.
            non_peak_hours += 24

    return peak_hours, non_peak_hours
