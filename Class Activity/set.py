sno = {1,1,3,2,3}
sstr = {'a','b','c'}
smix = {3,2,'a',True,(1,2,3)} # list, dict & set cant be in a set


print(sno,sstr,smix)

l2s = set([1,2,3])
print(type(l2s), l2s)

t2s = set((1,2,3))
print(type(t2s), t2s)
sno.add(5)
print(sno)
sno.update([7,8,9])
print(sno)
sno.remove(2)
print(sno)
sno.add(5)
print(sno)
sno.update([1,2])
print(sno)
sno.discard(4)
print(sno)
sno.pop()
print(sno)


smix.add(4)
print(smix)

print('a' in sstr)
print(1 in sstr)

print({1,2,3} is {1,2,3})
print(sstr is sstr)


a = {1,2,3,4,5}
b = {3,4,5,6,7}
c = {1,2}
print('union ' , a.union(b))
print("union using | ", a | b)
print('intersection' , a.intersection(b))
print("intersection using & ", a & b)
print("difference ", a.difference(b))
print("difference using - ", a - b)
print("symmetric difference ", a.symmetric_difference(b))
print("symmetric difference using ^ ", a ^ b)


print("equal           ", c == a)
print("not equal       ", c != a)

print("proper subset   ", c < a)
print("subset          ", c.issubset(a))
print("subset using <= ", c <= a)

print("proper superset ", c > a)
print("superset        ", c.issuperset(a))
print("superset using >= ", c >= a)

print("disjoint        ", c.isdisjoint(a))

fset = frozenset(c)
print(type(fset))


