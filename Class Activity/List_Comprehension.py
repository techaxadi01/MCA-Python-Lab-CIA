# Cartesian product of two lists (Nested loop vs List comprehension)

l1 = ['Christ', 'Jain']
l2 = ['college', 'University']

# Method 1: Using nested for loops
for i in l1:
    for j in l2:
        print(i + ' ' + j)

# Method 2: Using nested list comprehension
# Syntax: [expression for outer_item in list1 for inner_item in list2]
res = [x + ' ' + y for x in l1 for y in l2]
print(res)

# Note:
# Both approaches produce all 4 combinations: len(l1) * len(l2) = 4.
# List comprehension is more concise and generally faster in Python.