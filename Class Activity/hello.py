print("LIST Methods")

L1 = [1,2,3,4,6,6,7]
print(" L1 =  ", L1)

L1.insert(4,5)
print(" Inserst 5 =  ", L1)

L1.append(7)
print(" Append 7 =  ", L1)

L1.remove(7)
print(" Remove 7 =  ", L1)

L1.pop(6)
print(" Pop index 6 =  ", L1)

L1.clear()
print(" Clear =  ", L1)



L2 = [1,2,3,4,5]

L_copy = L2.copy()
print(L_copy)

L2T = tuple(L2)
print(type(L2T), L2T)

T1 = (6,7,8,9,10)
T2L = list(T1)
print(type(T2L), T2L)


a = [1,2,3]
b = [4,5,6]

print(a+b)
print(a.extend(b))

for i in b:
	a.append(i)
print(a)





