# https://youtu.be/jTYiNjvnHZY


# iterable: something that can be looped over (E.g. list)

# iterable: E.g. tuples dictionaries strings files generators and all kinds of different objects


"""
nums = [1, 2, 3]

names = ['Joseph', 'Corey']

for num in nums:
    print(num)
"""

# 🧠 dir()
# 😎 as long as we see __iter__ -> it's iterable

# for i in dir(nums):
#     print(i)

# ✅ test if an item is in a for loop
# Ref - https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/

"""
for i in dir(names):
    print(i)

if ('__iter__' in dir(names)):
    print('Element exists!')
"""

"""
iterator: is an object with a state so
that it remembers where it is during
iteration now I know all of these terms
might be running together
"""

"""
nums = [1, 2, 3]

i_nums = iter(nums)
# i_nums = nums.__iter__()

# print(i_nums)
# print(dir(i_nums))

print(next(i_nums))
print(next(i_nums))
print(next(i_nums))


class MyRange():

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = MyRange(1, 10)

for num in nums:
    print(num)
"""


"""
iterable: more specifically it means that the object needs to return an iterator
object from its dunder itter method and the iterator that is returned from dunder 
itter must define a dunder next method which accesses elements in the container one at a time
"""


def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


nums = my_range(1, 10)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
