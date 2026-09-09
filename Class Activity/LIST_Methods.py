# List Methods and Operations

print("LIST Methods")

# --- Basic List Methods (Mutation) ---
L1 = [1, 2, 3, 4, 6, 6, 7]
print(" L1 =  ", L1)

# insert(index, value) - inserts 5 at index 4
L1.insert(4, 5)
print(" Inserst 5 =  ", L1)

# append(value) - adds 7 to the end of the list
L1.append(7)
print(" Append 7 =  ", L1)

# remove(value) - removes first occurrence of 7 (throws ValueError if not present)
L1.remove(7)
print(" Remove 7 =  ", L1)

# pop(index) - removes and returns item at index 6 (if index not given, pops last item)
L1.pop(6)
print(" Pop index 6 =  ", L1)

# clear() - removes all elements, list becomes empty []
L1.clear()
print(" Clear =  ", L1)


# --- Copying a List ---
L2 = [1, 2, 3, 4, 5]

# copy() creates a shallow copy
L_copy = L2.copy()
print(L_copy)


# --- Type Conversions (List <-> Tuple) ---
# list to tuple
L2T = tuple(L2)
print(type(L2T), L2T)

# tuple to list
T1 = (6, 7, 8, 9, 10)
T2L = list(T1)
print(type(T2L), T2L)


# --- Combining Lists ---
a = [1, 2, 3]
b = [4, 5, 6]

# 1. Using + operator (returns a new list)
print(a + b)

# 2. Using extend()
# Note: extend() modifies 'a' in-place and returns None, so print(...) shows None
print(a.extend(b))

# 3. Using a loop to append elements one by one
for i in b:
    a.append(i)
print(a)
