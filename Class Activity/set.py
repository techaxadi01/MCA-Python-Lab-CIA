# Set data structure, methods, and mathematical operations

# --- 1. Set Creation and Characteristics ---
# Duplicates are automatically removed: {1, 1, 3, 2, 3} -> {1, 2, 3}
sno = {1, 1, 3, 2, 3}
sstr = {'a', 'b', 'c'}

# Sets can only contain immutable (hashable) items
# Note: True and 1 have same hash value (True == 1), so only one is kept
smix = {3, 2, 'a', True, (1, 2, 3)} # list, dict & set cant be in a set

print(sno, sstr, smix)

# --- 2. Type Conversion to Set ---
l2s = set([1, 2, 3])
print(type(l2s), l2s)

t2s = set((1, 2, 3))
print(type(t2s), t2s)

# --- 3. Adding and Removing Elements ---
# add() - adds a single element
sno.add(5)
print(sno)

# update() - adds multiple elements from list/tuple
sno.update([7, 8, 9])
print(sno)

# remove() - removes item, raises KeyError if not found
sno.remove(2)
print(sno)

# adding existing element does nothing (no duplicates)
sno.add(5)
print(sno)

sno.update([1, 2])
print(sno)

# discard() - removes item, but does NOT raise error if missing
sno.discard(4)
print(sno)

# pop() - removes an arbitrary element (sets are unordered)
sno.pop()
print(sno)

smix.add(4)
print(smix)

# --- 4. Membership ('in') and Identity ('is') ---
# 'in' checks value presence (O(1) average lookup)
print('a' in sstr)
print(1 in sstr)

# 'is' checks memory location (id)
print({1, 2, 3} is {1, 2, 3})  # False: two different objects in memory
print(sstr is sstr)            # True: same reference

# --- 5. Mathematical Set Operations ---
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
c = {1, 2}

# Union (all unique items from both)
print('union ' , a.union(b))
print("union using | ", a | b)

# Intersection (items present in both)
print('intersection' , a.intersection(b))
print("intersection using & ", a & b)

# Difference (items in 'a' but not in 'b')
print("difference ", a.difference(b))
print("difference using - ", a - b)

# Symmetric difference (items in either a or b, but not both)
print("symmetric difference ", a.symmetric_difference(b))
print("symmetric difference using ^ ", a ^ b)

# --- 6. Set Comparisons / Relations ---
print("equal           ", c == a)
print("not equal       ", c != a)

# Subset and Proper Subset
print("proper subset   ", c < a)
print("subset          ", c.issubset(a))
print("subset using <= ", c <= a)

# Superset and Proper Superset
print("proper superset ", c > a)
print("superset        ", c.issuperset(a))
print("superset using >= ", c >= a)

# Disjoint (True if sets have no common elements)
print("disjoint        ", c.isdisjoint(a))

# --- 7. Frozen Set ---
# frozenset is an immutable set (can be used as dictionary key or set element)
fset = frozenset(c)
print(type(fset))
