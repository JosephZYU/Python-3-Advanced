# https://youtu.be/Qu3dThVy6KQ

import itertools
import operator

from snippets_people import people

"""
counter = itertools.repeat(2, times=3)
squares_star = itertools.starmap(
    pow, [(0, 2), (1, 2), (2, 2)])  # square 1 of 2

print(next(counter))
print(next(counter))
print(next(counter))

print(list(squares_star))

# counter = itertools.cycle(('On', 'Off'))
# counter = itertools.count()

# 🧠 map(pow, range(), itertools.repeat())
# 😎 Great for repetitive tasks

expos = map(pow, range(1, 11), itertools.repeat(3))
squares_map = map(pow, range(1, 11), itertools.repeat(2))  # square 2 of 2


print(list(squares_map))
print(list(expos))

# print(next(counter))
# print(next(counter))
# print(next(counter))


data = list(range(100, 500, 100))

# 🧠 itertools.count(start= , step=)

daily_data = list(zip(itertools.count(start=5, step=5), data))

print(daily_data)
"""

# Combinations (order doesn't matter) and Permutations (order does matter)


def lt_2(n):
    """create custom-functino to filter ONLY value less than 2"""
    if n < 2:
        return True
    return False

# 🎯 How-to create symmetric list


letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 2, 1, 0]
names = ['Corey', 'Nicole']

selectors = [True, True, False, True]

# ✅ How-to import a varibale from another file in the same directory
# Ref - https://stackoverflow.com/a/17255770


# 🧠 itertools.combinations(list, 2)
results_com = itertools.combinations(letters, 2)

for item in results_com:
    print(item)

print()

# 🧠 itertools.permutations(list, 2)
results_per = itertools.permutations(letters, 2)

for item in results_per:
    print(item)

print()

# 🧠 itertools.product(list, 2)
results_prod = itertools.product(numbers, repeat=4)

for item in results_prod:
    print(item)

print()

# 🧠 itertools.combinations_with_replacement(list, 2)
results_replace = itertools.combinations_with_replacement(numbers, 4)

for item in results_replace:
    print(item)

print()


# 😎 Create chained list == Extremely Efficient for Bid Data

combined = itertools.chain(letters, numbers, names)

for item in combined:
    print(item)

print()

# Slicing combined chain
# 😎 Great for memory-efficiency: store your variable as an "idea", not in memory!

results_slice = itertools.islice(range(10), 1, 5, 2)

for item in results_slice:
    print(item)

print()

# 👍 Real-World Example
with open('test.log', 'r') as f:
    header = itertools.islice(f, 3)

    for line in header:
        print(line, end='')

print()

# 🧠 itertools.compress(letters, selectors)
# 😎 Use compress to "pass in" True/False as iterable!

results_compress = itertools.compress(letters, selectors)

for item in results_compress:
    print(item)

print()

# 🧠 filter(filter_func, list)

results_filter = itertools.filterfalse(lt_2, numbers)
# results_filter = filter(lt_2, numbers)

for item in results_filter:
    print(item)

print()

# 🧠 itertools.dropwhile(filter_func, list)

results_drop = itertools.dropwhile(lt_2, numbers)
for item in results_drop:
    print(item)

print()


# 🧠 itertools.takewhile(filter_func, list)

results_take = itertools.takewhile(lt_2, numbers)
for item in results_take:
    print(item)

print()


# 🧠 itertools.accumulate(numbers)

results_accu = itertools.accumulate(numbers)
for item in results_accu:
    print(item)

print()


# 🧠 itertools.accumulate(numbers, operator.mul)
# Creating running products 🏃‍♂️💨

results_mul = itertools.accumulate(numbers, operator.mul)

for item in results_mul:
    print(item)

print()

# 😎 Simulate Group-by function from Excel


def get_state(person):
    return person['state']


person_group = itertools.groupby(people, get_state)

# for (key, group) in person_group:
#     print(key)
#     for person in group:
#         print(person)
#     print()

for (key, group) in person_group:
    print(key, len(list(group)))


# Replicate an iterator

copy1, copy2 = itertools.tee(person_group)

for (key, group) in person_group:
    print(key, len(list(group)))
