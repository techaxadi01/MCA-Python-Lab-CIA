# Write a Python Prog to check the string is a palindrome or not

ch = 1
st = input("Enter a String : ")

s2 = st[::-1]

if st == s2:
	print ("palindrome")
else:
	print("not palindrome")