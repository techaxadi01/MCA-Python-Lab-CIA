   def c2f(c):
	return (c**9/5)+32
def f2c(f):
	return (f-32)*5/9

c= 32
print(c2f(c))
f= 100
print(f2c(f))



def mrk_ana(mrks):
	total = sum(mrks)
	avg = total/len(mrks)
	hi = max(mrks)
	lo = min(mrks)

	return total,avg,hi, lo

mrk = [54,5,46,48,54]
total, avg, hi, lo = mrk_ana(mrk)
print(total, avg, hi, lo)

def pw_val(pw):
	if len(pw) >= 8:
		for i in pw:
			if i.isdigit():
				return 'PW ok'
		return 'No num'
	else:
		return 'not 8 char'

pw1='fgsfgszg4'
pw2='sfgf45'
pw3='dfasfdggda'

print(pw_val(pw1))
print(pw_val(pw2))
print(pw_val(pw3))


# Attend % 

def Att_per(att_dict):
	t_day,p =0,0
	att_p = dict()
	for key in att_dict.keys():
		for a in att_dict[key]:
			t_day+=1
			p+=a
		att_p[key]=p/t_day

	return att_p

att = {
	'adi':[1,0,1,1,0],
	'di':[1,0,1,0,0],
	'av':[1,1,1,1,0]
}

print(Att_per(att))
