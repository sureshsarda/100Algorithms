from datetime import datetime
from dateutil.relativedelta import relativedelta


def humanized_relative_delta(relativedelta, sep=' ', sep_2=' ', just_now='just now'):
    DURATIONS = ['years', 'months', 'days', 'hours', 'minutes', 'seconds']
    humanized = []
    for duration in DURATIONS:
        if relativedelta.__getattribute__(duration):
            val = relativedelta.__getattribute__(duration)
            assert val >= 1
            if val <= 1:
                duration = duration.rstrip('s')

            msg = '{0}{1}{2}'.format(val, sep_2, duration)
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


    datetime.