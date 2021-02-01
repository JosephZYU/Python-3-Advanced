# 🧭 Multiprocessing is EVEN faster than Threading - the Ultimate concurrent model
# 多重处理 比 线程处理 更快！ 终极的算力表现！

import multiprocessing
import time

# 🧠 ⏰ Use time to measure how long it took the func to run ⌛️
start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping for {seconds} seoncd ...')
    time.sleep(seconds)
    print('Done Sleeping')


"""
# Perform the function
do_something(1)
do_something(1)
"""

"""
# NOTE: ONLY the func w/o the ()! # NOT do_something()
p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

# Make sure you would actually start the process
p1.start()
p2.start()

p1.join()
p2.join()

"""

# Append Each process to a list and save it
# Looking through a range of 10
# Each time, creating this new target of do_something

prcesses = []

for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=[1.5])
    p.start()
    prcesses.append(p)

for process in prcesses:
    process.join()


# Calculate the finish time
finish = time.perf_counter()

print(f'Script finished in {round(finish-start, 2)} second(s)')
