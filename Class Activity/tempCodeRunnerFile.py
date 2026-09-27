# Defauolt Argument

class Patient:
    def reggg (self, name, age = 0, disease = "Not Sepcified"):
        print("Name : ", name)
        print("Age : ", age)
        print("Desease : ", disease)

p = Patient()

p.reggg(30, "Specified")
print()

class Patient1:
    def regg1 (self, *details):

        if len(details) == 1:
            print("Name : ", details[0])

        elif len(details) == 2:
            print("Name : ", details[0])
            print("Age : ", details[1])

        elif len(details) == 3:
            print("Name : ", details[0])
            print("Age : ", details[1])
            print("Desease : ", details[2])

        else:
            print("TOO LOW OR LARGE NO OF ARGG")

p1 = Patient1()

p1.regg1("ANU")
print()
p1.regg1("Ravi",25)
print()
p1.regg1("Meena",30,"Diabetes")