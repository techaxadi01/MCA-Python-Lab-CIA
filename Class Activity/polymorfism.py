# Polymorfism - 

class Patient:
    def consultation(self):
        print("general consultation")

class CardiologyPatient(Patient):
    def consultation(self):
        print("cardiology consultation")

class OrthopedicPatient(Patient):
    def consultation(self):
        print("orthopedic consultation")

# Creating objects
p1 = CardiologyPatient()
p2 = OrthopedicPatient()

# Calling the polymorphic method
p1.consultation() 
p2.consultation()

# Polymorfism with a comman Interface 

class Patient1:
    def treatment(self):
        print("General Treatment")

class DiabetesPatient1(Patient1):
    def treatment(self):
        print("Diiabetes Management")

class HeartPatient1(Patient1):
    def treatment(self):
        print("Heart Management")

patients = [Patient1(), HeartPatient1(), HeartPatient1()]

for patient in patients:
    patient.treatment()



# Polymorfism with different classes

class Doctor:
    def work(self):
        print("Doctor")

class Nurce:
    def work(self):
        print("Nurce")

class Phrmascits:
    def work(self):
        print("Phrmascits")


works = [Doctor(), Nurce(), Phrmascits()]

for work in works:
    work.work()




# Abstract class an abstrat class is a blueprinnt that defines what a child class must do, but leaves the actual implementation to the child class

# Every child class must provide these methods, but each child can implement them directly 


from abc import ABC, abstractmethod

class Patient_ABC:
    def __init__(self, patient_id, name):
        self.patient_id =patient_id
        self.name = name

    def display(self):
        print("patient_id : ", self.patient_id)
        print("name : ", self.name)

    @abstractmethod
    def treatement(self):
        pass 

class CardiacPatient2(Patient_ABC):
    def treatement(self):
        print("Treatment : Cardiac Care") 

class OrthopedicPatient2(Patient_ABC):

	def treatement (self):
		print("treatement : orthopedic care")

class DiabeticPatient2(Patient_ABC):
	def treatement(self):
		print("treatement: diabetes management")


#Creating objects
p1 = CardiacPatient2(101,"Anu")
p2 = OrthopedicPatient2(102,"Ravi")
p3 = DiabeticPatient2(103,"Meena")

# Calling methods
p1.display()
p1.treatement()

p2.display()
p2.treatement()

p3.display()
p3.treatement()
