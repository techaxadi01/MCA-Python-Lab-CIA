# Program: Check whether a string is a palindrome or not

ch = 1
st = input("Enter a String : ")

# string slicing: [start:stop:step]
# step = -1 reverses the string
s2 = st[::-1]

if st == s2:
    print("palindrome")
else:
    print("not palindrome")
