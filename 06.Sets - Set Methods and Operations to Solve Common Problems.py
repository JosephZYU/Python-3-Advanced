# https://youtu.be/r3R3h5ly_8g
"""
# 🧠 set([list])

# Methods to create set"
# 1 of 2: set([list])
# 2 of 2: {list}

# A set is a list that removes ALL duplicated values

s1 = set([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
print(s1)

# 🧠 set.add()
s1.add(6)
print(s1)

# 🧠 set.update()

s1.update([7, 8, 9])
print(s1)

s2 = {6, 7, 8, 9}

s1.update(s2)
print(s1)

# 😎 No matter how many *iterables we add to the set
s1.update([7, 8, 9], s2)
print(s1)

# 🧠 set.remove()
s1.remove(6)
s1.remove(7)
s1.remove(8)
s1.remove(9)
print(s1)

# 🧠 set.discard()

s1.discard(6)
print(s1)
"""

"""
# 🧠 s1.intersection(s2)
# Create intersection

s3 = {3, 4, 5}
s4 = {4, 5, 6}
s5 = {5, 6, 7}

s6 = s3.intersection(s4)
print(s6)

# 😎 intersectino of ALL three sets from above
s7 = s3.intersection(s4, s5)
print(s7)

# Return the difference
# 👀 included in the base. NOT in the (list)

s8 = s3.difference(s4)
print(s8)

s9 = s4.difference(s3)
print(s9)

# 🧠 s1.symmetric_difference(s2)

s10 = s3.symmetric_difference(s4)
s11 = s4.symmetric_difference(s3)

print(s10)
print(s11)

print(s10 is s11)
print(id(s10))
print(id(s11))

print(s10 == s11)
"""


l0 = list(range(1, 6))
l1 = [1, 2, 3, 3, 2, 1]
l2 = set(l1)

print(l1)
print(l2)


employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

# 🔬 Test if all arrangements of intersection() yield the SAME results
# ✅ YES - that are all the SAME!
# 🧠 s1.intersectino(*iterable)
# intersection -> ABSOLUTE intersections

s12 = set(employees)
s13 = set(gym_members)
s14 = set(developers)

print(s12.intersection(s13, s14))
print(s13.intersection(s12, s14))
print(s14.intersection(s13, s12))
print()

print(s12.difference(s13, s14))
print(s13.difference(s12, s14))
print(s14.difference(s13, s12))
print()

if 'Corey' in s12:
    print('Found!')

# 🧭 O(n) for list  # traverse the WHOLE list then return
# 🧭 O(1) - a constant 1 for set #


# 🎯 TODO - create 'Found' mechasnism for instance O(1) search results
"""for (a, b, c) in zip(s12, s13, s14):
    print('Found!')"""
