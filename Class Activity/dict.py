std = {'regno':2647203,'name':'Adi','cls':'1MCAB','age':21}

print(std)
print(type(std))

print(std['regno'],std['name'],std['cls'],std['age'])
print(std.get('name'))

# print(std['mrk'])   gives error
print(std.get('mrk'))   #does not give error 
print(std)

std['mrk']=83
print(std)

std.update({'age':20,'mrk':91}) # key should be there
std.update({'no':1})
print(std)

print(std.items())
print(type(std.items()))
for k,v in std.items():
    print(k,':',v)

print('keys :', std.keys())
print('val :', std.values())

cpy = std.copy()
print('cpy :',cpy)
print(cpy.clear())

#print(std.pop())    Gives error needs key as parameter
print(std.pop('no'))
print(std)
print(std.popitem())
print(std)

# Dictinory Comprehension
no = [1,2,3,4,5]
sq = {n : n*n for n in no}
print(sq)
even = {n:n*n for n in no if n%2==0}
print(even)

no1 = range(1,11)
even1 = {n:n*n for n in no1 if n%2==0}
print(even1)

#nested dict
stds = {
    '2647203': {
        'name': 'Adi',
        'mrks': {
            'python': 85,
            'dsa': 90,
            'stats': 78
        }
    },
    '2647204': {
        'name': 'Abhishek',
        'mrks': {
            'python': 92,
            'dsa': 88,
            'stats': 85
        }
    }
}

print(stds)
print(stds['2647203']['name'])
print(stds['2647203']['mrks']['python'])

mrksum = 0
count = 0
for mk in stds['2647204']['mrks'].values():
	count += 1
	mrksum += mk
print('Avg mrk', round(mrksum/count,2))

test = {1 : 'a',2:'b'}
print(test[1])