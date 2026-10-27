
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self):
        discount = self.get_bill_amount() * 0.20
        return self.get_bill_amount() - discount


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        discount = self.get_bill_amount() * 0.15
        return self.get_bill_amount() - discount

print("RALPHIEE-CHAN BILLING SYSTEM")

name = input("Enter patient name: ")
bill_amount = float(input("Enter bill amount: "))

print("\nPatient Type:")
print("1. Regular Patient")
print("2. Senior Citizen")
print("3. PhilHealth Member")

choice = input("Choose patient type (1 taman 3): ")

if choice == "1":
    patient = Patient(name, bill_amount)
elif choice == "2":
    patient = SeniorPatient(name, bill_amount)
elif choice == "3":
    patient = PhilHealthPatient(name, bill_amount)
else:
    print("Invalid patient type.")
    exit()

print("\nORIGINAL BILL VS FINAL BILL AURA BATTLE")
print("Patient Name:", patient.get_name())
print("Original Bill: In Pesos", format(patient.get_bill_amount()))
print("Final Bill: In Pesos ", format(patient.calculate_bill()))
