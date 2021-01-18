"""Convert date/time into a string relative to now.

Possible input types:
* time.time()
* datetime.date.today()
* datetime.datetime.now()

Output:
    <int> <unit> <text>

Examples:
```python
import datetime
from RelativeToNow import relative_to_now

print(relative_to_now(datetime.datetime.now() + datetime.timedelta(days=1)))
>>> 1 day from now
```

Precision for `datetime.date` is days.
```python
import datetime
from RelativeToNow import relative_to_now

print(relative_to_now(datetime.date.today() - datetime.timedelta(days=1)))
>>> 1 day ago
```

```python
import time
from RelativeToNow import relative_to_now

print(relative_to_now(time.time()))
>>> 0 seconds from now
```
"""


import datetime
import time


def relative_to_now(start_date):
    if isinstance(start_date, datetime.datetime):
        diff = datetime.datetime.now() - start_date
        abs_seconds = diff.days * 3600 * 24 + diff.seconds
    elif isinstance(start_date, datetime.date):
        diff = datetime.date.today() - start_date
        abs_seconds = diff.days * 3600 * 24 + diff.seconds
    elif isinstance(start_date, float):  # noqa: SIM106
        abs_seconds = int(time.time() - start_date)

    else:
        raise Exception("type must be date or datetime.")

    my_text = "ago" if abs_seconds > 0 else "from now"
    abs_seconds = abs(abs_seconds)

    seconds = abs_seconds // 1

    if seconds == 0:
        return "just now"

    elif seconds < 60:
        unit = "second" if seconds == 1 else "seconds"
        return "%s %s %s" % (seconds, unit, my_text)

    minutes = abs_seconds // 60
    if minutes < 60:
        unit = "minute" if minutes == 1 else "minutes"
        return "%s %s %s" % (minutes, unit, my_text)

    hours = abs_seconds // 3600
    if hours < 24:
        unit = "hour" if hours == 1 else "hours"
        return "%s %s %s" % (hours, unit, my_text)

    days = abs_seconds // (3600 * 24)
    if days < 7:
        unit = "day" if days == 1 else "days"
        return "%s %s %s" % (days, unit, my_text)

    weeks = abs_seconds // (3600 * 24 * 7)
    if weeks < 52:
        unit = "week" if weeks == 1 else "weeks"
        return "%s %s %s" % (weeks, unit, my_text)

    years = abs_seconds // (3600 * 24 * 365)
    if years >= 1:
        unit = "year" if years == 1 else "years"
        return "%s %s %s" % (years, unit, my_text)

    return start_date
