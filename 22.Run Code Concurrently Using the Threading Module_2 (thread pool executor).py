import concurrent.futures

import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping for {seconds} second(s) ...\n')
    time.sleep(seconds)
    print('Done Sleeping ...\n')

# 🆕 ThreadPoolExecutor


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = range(5, 0, -1)  # [5, 4, 3, 2, 1]

    # results = [executor.submit(do_something, sec) for sec in secs]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

    for f in concurrent.futures.as_completed(results):
        print(f.result())
"""
    # (func, wait_time)
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)
    print(f1.result())
    print(f2.result())
"""


finish = time.perf_counter()
print(f'Task finished in {finish:,.2f} second(s)')
