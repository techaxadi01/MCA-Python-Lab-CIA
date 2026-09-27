class Account: # empty type
    pass

a1 = Account() # Constructor call
a2 = Account()
a1.name = 'Jhon' # sttribute assignment
a1.balance = 1000

a2.surname = "Kumar"
a2.value = 101010
a2.balance = 1200

print(id(Account))

print(a2)
print(a1.balance)
print(a2.surname)
# print(a1.surname) # give error as a1.surname is not defined



# self -  refer to the current instance / object 
# __init__() method is commanly used to initalize an object's attribute when the object is created
# Amethod is a function defined inside a class

class Patient:

    def __init__(self,patient_id,name, age, diagonosis):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagonosis = diagonosis

    def display(self):
        print("Patient ID: ",self.patient_id)
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Diagonosis: ",self.diagonosis)

    def is_senior(self):
        return self.age >= 60

    

p1 = Patient("p101","Ananya",35,"Diabetes")
p2 = Patient("p102","Ravi",65,"Hypertension")

p1.display()
print("senior:",p1.is_senior())

print()
p2.display()
print("senior:",p2.is_senior())




# crete a class std with 3 method cal total, avg , display the std detail, display the result

class Std:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def cal_total(self):
        return sum(self.marks)

    def cal_avg(self):
        return self.cal_total() / len(self.marks)

    def grade(self):
        if self.cal_avg() >= 90:
            return "A+"
        elif self.cal_avg() >= 80:
            return "A"
        elif self.cal_avg() >= 70:
            return "B"
        elif self.cal_avg() >= 60:
            return "C"
        elif self.cal_avg() >= 50:
            return "D"
        else:
            return "Fail"

    def cal_result(self):
        self.result = "Pass"
        for mrk in self.marks:
            if mrk < 40:
                self.result = "Fail"
                break
        return self.result

    @staticmethod
    def university_name():
        print("CHRIST UNIVERSITY")

    def display(self):
        print("\nStudent Details")
        print("Roll No: ", self.roll_no)
        print("Name: ", self.name)
        print("Marks: ", self.marks)
        print("Total: ", self.cal_total())
        print("Average: ", self.cal_avg())
        print("Grade: ", self.grade())
        print("Result: ", self.cal_result())


student1 = Std(1, "Rahul", [85, 90, 80])
Std.university_name()
student1.display()



#Types of methods in python 
#1. instance Method - works with individual object data.
class Patient1:

    def display(Self):
	    print("Patient details")

p1=Patient1()
p1.display()

#2. class Method-work with class-level data.
class Patient2:

	hospital_name = "ABC Hospital"
	
	@classmethod
	def display_hospital(cls):
	    print(cls.hospital_name)

Patient2.display_hospital()

#3. static method - a static method does not depend on instance or class data . 
class Patient3:

	@staticmethod
	def hospital_tamings():
		print("Hospital Timing : 9 am - 5 PM")

Patient3.hospital_tamings()




# Inheritance


# 1. Single Inheritance
# One child class inherits from one parent class

class P_Patient1:
    def show_patient(self):
        print("Patient ID: P001")
        print("Name: Adi")

class C_Patient1(P_Patient1):
    def show_room(self):
        print("Room No: 203")

patient = C_Patient1()
patient.show_patient()
patient.show_room()


# 2. Multiple Inheritance
# One child class inherits from more than one parent class

class P1_Patient2:
    def show_patient(self):
        print("Patient ID: P002")

class P2_Patient2:
    def billing(self):
        print("Consultant Fee: Rs 500")

class C_Patient2(P1_Patient2, P2_Patient2):
    def show_room(self):
        print("Room No: 204")

patient = C_Patient2()
patient.show_patient()
patient.billing()
patient.show_room()


# 3. Multilevel Inheritance
# A child class inherits from another child class

class P_Patient3:
    def show_patient(self):
        print("Patient ID: P003")

class C1_Patient3(P_Patient3):
    def billing(self):
        print("Consultant Fee: Rs 500")

class C2_Patient3(C1_Patient3):
    def show_room(self):
        print("Room No: 205")

patient = C2_Patient3()
patient.show_patient()
patient.billing()
patient.show_room()


# 4. Hierarchical Inheritance
# More than one child class inherits from one parent class

class P_Patient4:
    def show_patient(self):
        print("Patient ID: P004")

class C1_Patient4(P_Patient4):
    def show_room(self):
        print("Room No: 206")

class C2_Patient4(P_Patient4):
    def billing(self):
        print("Consultant Fee: Rs 500")

patient1 = C1_Patient4()
patient1.show_patient()
patient1.show_room()

patient2 = C2_Patient4()
patient2.show_patient()
patient2.billing()


# 5. Hybrid Inheritance
# Combination of two or more types of inheritance

class P_Patient5:
    def show_patient(self):
        print("Patient ID: P005")

class C1_Patient5(P_Patient5):
    def show_room(self):
        print("Room No: 207")

class C2_Patient5(P_Patient5):
    def billing(self):
        print("Consultant Fee: Rs 500")

class C3_Patient5(C1_Patient5, C2_Patient5):
    def show_doctor(self):
        print("Doctor: Dr. Ravi")

patient = C3_Patient5()
patient.show_patient()
patient.show_room()
patient.billing()
patient.show_doctor()

