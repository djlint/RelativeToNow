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


def relative_to_now(start_date, no_error=False):
    """Verify date and return converted."""
    if isinstance(start_date, datetime.datetime):
        if start_date.tzinfo:
            diff = datetime.datetime.now(start_date.tzinfo) - start_date
        else:
            diff = datetime.datetime.now() - start_date
        abs_seconds = diff.days * 3600 * 24 + diff.seconds

    elif isinstance(start_date, datetime.date):
        diff = datetime.date.today() - start_date
        abs_seconds = diff.days * 3600 * 24 + diff.seconds

    elif isinstance(start_date, float):  # noqa: SIM106
        abs_seconds = int(time.time() - start_date)

    else:
        if no_error:
            return start_date

        raise Exception("type must be date or datetime.")

    return convert(abs_seconds, start_date)


def build_string(unit, value, my_text):
    """Build string from params."""
    unit = unit if value == 1 else unit + "s"
    return "%s %s %s" % (value, unit, my_text)


def convert(abs_seconds, output):
    """Convert date to string."""
    my_text = "ago" if abs_seconds > 0 else "from now"
    abs_seconds = abs(abs_seconds)

    seconds = abs_seconds // 1
    minutes = abs_seconds // 60
    hours = abs_seconds // 3600
    days = abs_seconds // (3600 * 24)
    weeks = abs_seconds // (3600 * 24 * 7)
    years = abs_seconds // (3600 * 24 * 365)

    if seconds == 0:
        output = "just now"

    elif seconds < 60:
        output = build_string("second", seconds, my_text)

    elif minutes < 60:
        output = build_string("minute", minutes, my_text)

    elif hours < 24:
        output = build_string("hour", hours, my_text)

    elif days < 7:
        output = build_string("day", days, my_text)

    elif weeks < 52:
        output = build_string("week", weeks, my_text)

    elif years >= 1:
        output = build_string("year", years, my_text)

    return output
