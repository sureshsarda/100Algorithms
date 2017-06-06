from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def timedelta_to_relativedelta(tdelta):
    assert isinstance(tdelta, timedelta)

    seconds_in = {
        'year'  : 365 * 24 * 60 * 60,
        'month' : 30 * 24 * 60 * 60,
        'day'   : 24 * 60 * 60,
        'hour'  : 60 * 60,
        'minute': 60
    }

    years, rem = divmod(tdelta.total_seconds(), seconds_in['year'])
    months, rem = divmod(rem, seconds_in['month'])
    days, rem = divmod(rem, seconds_in['day'])
    hours, rem = divmod(rem, seconds_in['hour'])
    minutes, rem = divmod(rem, seconds_in['minute'])
    seconds = rem

    return relativedelta(years=years, months=months, days=days, hours=hours, minutes=minutes, seconds=seconds)


def humanized_relative_delta(delta, sep=' ', sep_2=' ', just_now='just now'):
    if isinstance(delta, timedelta):
        delta = timedelta_to_relativedelta(delta)

    DURATIONS = ['years', 'months', 'days', 'hours', 'minutes', 'seconds']
    humanized = []
    for duration in DURATIONS:
        if delta.__getattribute__(duration):
            val = delta.__getattribute__(duration)
            assert val >= 1
            if val <= 1:
                duration = duration.rstrip('s')

            msg = '{0}{1}{2}'.format(int(val), sep_2, duration)
            humanized.append(msg)
    return sep.join(humanized) if humanized else just_now


if __name__ == '__main__':
    assert humanized_relative_delta(relativedelta(days=1)) == '1 day'
    assert humanized_relative_delta(relativedelta(days=2)) == '2 days'
    assert humanized_relative_delta(relativedelta(days=40)) == '40 days'
    assert humanized_relative_delta(relativedelta(years=10, days=40)) == '10 years 40 days'
    assert humanized_relative_delta(relativedelta(years=1)) == '1 year'
    assert humanized_relative_delta(relativedelta(minutes=1)) == '1 minute'
    assert humanized_relative_delta(relativedelta(hours=1, minutes=1, seconds=3)) == '1 hour 1 minute 3 seconds'
    assert humanized_relative_delta(relativedelta(years=1, minutes=1, seconds=3)) == '1 year 1 minute 3 seconds'
    assert humanized_relative_delta(relativedelta()) == 'just now'
    assert humanized_relative_delta(relativedelta(minutes=0)) == 'just now'

    print(humanized_relative_delta(datetime.now() - datetime(1971, 1, 1)))
