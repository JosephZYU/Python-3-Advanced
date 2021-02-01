import time

# Using from import -> we can get specific module without repeaing datetime.dt!
# 🧠 from A import a -> from import
from datetime import datetime as dt


# import datetime as dt

# 😎 Set it to None


def display_time(time_to_print=dt.now()):
    print(time_to_print.strftime('%B %d, %Y %H:%M:%S %f'))


# there is NO change at all! Even at the micro-second level!
display_time()
time.sleep(1)

display_time()
time.sleep(1)

display_time()
time.sleep(1)

print(display_time.__defaults__)


def display_time_fixed(time_to_print=None):
    if time_to_print is None:
        time_to_print = dt.now()
    print(time_to_print.strftime('%B %d, %Y %H:%M:%S %f'))


display_time_fixed()
time.sleep(1)

display_time_fixed()
time.sleep(1)

display_time_fixed()
time.sleep(1)
