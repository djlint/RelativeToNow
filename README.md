
<h1 align="center">Relative To Now</h1>

<h4 align="center">Convert date/time into a string relative to now.</h4>

<p align="center">
  <a href="https://pypi.org/project/relative-to-now/">
    <img src="https://img.shields.io/badge/Python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue" alt="Python Version">
  </a>
  <a href="https://codecov.io/gh/Riverside-Healthcare/RelativeToNow">
    <img src="https://codecov.io/gh/Riverside-Healthcare/RelativeToNow/branch/master/graph/badge.svg?token=PHYGI9FI22" alt="Codecov Status">
  </a>
  <a href="https://www.codacy.com/gh/Riverside-Healthcare/RelativeToNow/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Riverside-Healthcare/RelativeToNow&amp;utm_campaign=Badge_Grade">
    <img src="https://app.codacy.com/project/badge/Grade/2533c8838ffe4c6a82c889d6d98f2050" alt="Codacy Status">
  </a>
  <a href="https://pypi.org/project/relative-to-now/">
    <img src="https://badgen.net/pypi/v/relative-to-now" alt="Pypi Download">
  </a>
  <a href="https://pepy.tech/project/relative-to-now">
    <img src="https://static.pepy.tech/badge/relative-to-now" alt="Downloads">
  </a>
</p>


## 💾 Install

```sh
python -m pip install relative-to-now

# or

poetry add relative-to-now
```

## ✨ How to Use

Possible input types:

  * time.time()
  * datetime.date.today()
  * datetime.datetime.now()

Optional inputs:

  * ``no_errors`` (Defaults to ``False``, set to ``True`` to return value when there is an error instead of raising)

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
