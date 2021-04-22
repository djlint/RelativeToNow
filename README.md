[![Build Status](https://travis-ci.com/Riverside-Healthcare/RelativeToNow.svg?branch=master)](https://travis-ci.com/Riverside-Healthcare/RelativeToNow)
[![codecov](https://codecov.io/gh/Riverside-Healthcare/RelativeToNow/branch/master/graph/badge.svg?token=PHYGI9FI22)](https://codecov.io/gh/Riverside-Healthcare/RelativeToNow)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/2533c8838ffe4c6a82c889d6d98f2050)](https://www.codacy.com/gh/Riverside-Healthcare/RelativeToNow/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Riverside-Healthcare/RelativeToNow&amp;utm_campaign=Badge_Grade)
[![Code QL](https://github.com/Riverside-Healthcare/extract_management/workflows/CodeQL/badge.svg)](https://github.com/Riverside-Healthcare/extract_management/actions/workflows/codeql-analysis.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/9c289db00e2942b3ad8e/maintainability)](https://codeclimate.com/github/Riverside-Healthcare/RelativeToNow/maintainability)

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