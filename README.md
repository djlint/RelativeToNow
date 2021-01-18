# Relative To Now

Convert date/time into a string relative to now.

## Install

```sh
python -m pip install relative-to-now

# or

poetry add relative-to-now
```

## How to Use

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

print(relative_to_now(datetime.date.today() - datetime.timedelta(days=2)))
>>> 2 days ago
```

```python
import time
from RelativeToNow import relative_to_now

print(relative_to_now(time.time()))
>>> just now
```