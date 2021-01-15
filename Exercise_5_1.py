import time
import math

current_time=time.localtime()
print(current_time)
format_time=time.strftime("%H:%M:%S", current_time)
print(format_time)
seconds_since_epoch=time.time()
hours_since_epoch=seconds_since_epoch/3600
days_since_epoch=hours_since_epoch/24
print("Days since epoch time is: ", int(days_since_epoch), " days")