l1 = ['Christ','Jain']
l2 = ['college','University']

for i in l1:
	for j in l2:
		print(i + ' ' + j)

res = [x+' '+y for x in l1 for y in l2]
print(res)