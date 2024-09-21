import calendar

import click

from peak.peak import calculate_peak_and_nonpeak_hours


@click.group()
def cli():
    """
    Use this cli tool to calculate the peak
    and non-peak hours in a month. This will
    echo information to stdout.
    """


@click.command()
@click.argument("year", type=int)
@click.argument("month", type=int)
def get_hours(year: int, month: int):
    if not 1 <= month <= 12:
        click.echo(
            f"Failed to get hours for {month}, {year}:"
            f"{month} value is out of range. Please choose "
            f"a value from 1 - 12"
        )
        return
    peak, non_peak = calculate_peak_and_nonpeak_hours(year, month)
    month_name = calendar.month_name[month]
    click.echo(f"\nTotal Peak Hours in {month_name}, {year}: {peak} hours")
    click.echo(
        f"Total non-peak Hours in {month_name}, {year}: {non_peak} hours"
    )


cli.add_command(get_hours)
