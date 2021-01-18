import datetime
import time

from RelativeToNow import relative_to_now

print(relative_to_now(datetime.datetime.now() + datetime.timedelta(days=1)))


print(relative_to_now(datetime.date.today() - datetime.timedelta(days=1)))
print(relative_to_now(time.time()))
