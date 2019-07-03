from datetime import date

today = date.today()
c_year = today.year
c_month = today.month
c_day = today.day
total_employment = 0
options = ""
employers = []

class Employee:
	def __init__ (self, name, age, salary, employment_year):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_year = int(employment_year)

	def get_working_years(self):
		total_employment = int(c_year) - int(self.employment_year)
		return total_employment 

print ("Welcome to HR Fail 2020\n")

while options != "5":
	print ("Choose an Action\n")
	print ("\t1. Show Employees")
	print ("\t2. Show Managers")
	print ("\t3. Add an Employee")
	print ("\t4. Add a Manager")
	print ("\t5. Exit")

	options = input ("\nWhat would you like to do? ")

	if options == "3":

		x = Employee(input("Name: "),input("Age: "),input("Flosatik: "),input ("Employment Year: "))
		print(x.get_working_years())








