import re 

txt = "Welcome to the Regular Exprerestion Programmer in the Python Language"

search1 = re.search("he", txt)
print(search1)
print(search1.span())
print(search1.string)
print(search1.group())
fall1 = re.findall("he", txt)
print(fall1)
split1 = re.split("he", txt)
print(split1)
sub1 = re.sub("he", "5", txt)
print(sub1)


tx = "Welcomme to The re module moddule or concept on 29 Sep 2026 module moodle" # Gramatical Error on purpose to test all module

# Find any character from the set o, d, or u
s1 = re.findall("[odu]", tx)
print("s1:", s1)

# Match the word 'Welcome' with any two characters in the middle
s2 = re.findall("We..ome", tx)
print("s2:", s2)

# Match strings starting with 'Wel'
s3 = re.findall("^Wel", tx)
print("s3:", s3)

# Match a value ending with '26'
s1 = re.findall("26$", tx)
print("s1:", s1)

# Match 'mo' followed by any characters and ending in 'p'
s2 = re.findall("mo.*p", tx)
print("s2:", s2)

# Match 'module' with an optional single character between 'o' and 'ule'
s3 = re.findall("mo.?ule", tx)
print("s3:", s3)

# Match 'module' with one or more characters between 'o' and 'ule'
s1 = re.findall("mo.+ule", tx)
print("s1:", s1)

# Match 'mo' followed by exactly 3 characters and ending with 'e'
s2 = re.findall("mo.{3}e", tx)
print("s2:", s2)

# Match either 'module' or 'concept'
s3 = re.findall("module|concept", tx)
print("s3:", s3)

# Match either 'modle' or 'modle' using a capturing group
s1 = re.findall("mo(du|od)le", tx)
print("s1:", s1)

# Match either 'modle' or 'modle' using a non-capturing group
s2 = re.findall(r"mo(?:du|od)le", tx)
print("s2:", s2)

# Match strings that start with 'mo' and end with 'e' using *
s3 = re.findall(r"^mo*e$", tx)
print("s3:", s3)

# Match strings with 'mo' followed by zero or more 'o' and ending with 'e'
s1 = re.findall(r"mo*e$", tx)
print("s1:", s1)

# Match all alphabetic letters only
s2 = re.findall("[a-zA-Z]", tx)
print("s2:", s2)