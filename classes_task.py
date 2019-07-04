from datetime import date

today = date.today()
c_year = today.year
c_month = today.month
c_day = today.day
options = ""
employers = []
managers = []

class Employee:
	def __init__ (self, name, age, salary, employment_year):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_year = int(employment_year)

	def get_working_years(self):
		total_employment = int(c_year) - int(self.employment_year)
		return int(total_employment )

	def __str__(self):
		return "name: %s, age: %s, salary: %s working years: %s" % (self.name, self.age, self.salary, self.get_working_years())

class Manager(Employee):
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        Employee.__init__(self, name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage

    def get_bonus(self):
    	total_bonus = self.salary * self.bonus_percentage
    	return total_bonus

    def __str__(self):
    	return "name: %s, age: %s, salary: %s working years: %s, yearly bonus: %s" % (self.name, self.age, self.salary, self.get_working_years(), self.get_bonus())

print ("Welcome to HR Fail 2020")

while options != "5":
	print ("\nChoose an Action\n")
	print ("\t1. Show Employees")
	print ("\t2. Show Managers")
	print ("\t3. Add an Employee")
	print ("\t4. Add a Manager")
	print ("\t5. Exit")

	options = input ("\nWhat would you like to do? ")

	if options == "3":
		x = Employee(input("Name: "),input("Age: "),input("Flosatik: "),input ("Employment Year: "))
		x.get_working_years()
		print ("Employ added succesfully")
		employers.append(x)
	elif options == "1":
		if len(employers) == 0:
			print ("\nThere are currently no Employers")
		else:
			print ("\nEmployer(s)")
			for y in employers:
				print (y)
	elif options == "4":
		x = Manager(input("Name: "),input("Age: "),int(input("Flosatik: ")),input ("Employment Year: "), float(input ("Yearly Bonus: ")))
		x.get_working_years()
		x.get_bonus()
		print ("Employ added succesfully")
		managers.append(x)
	elif options == "2":
		if len(managers) == 0:
			print ("\nThere are currently no Managers")
		else:
			print ("\nEmployer(s)")
			for y in managers:
				print (y)
	elif options == "5":
		print("----------------")
		print ("Thank you for using HR Fail 2020 =)")
		print("----------------")
		break
	else:
		print ("\nPlease pick an option from 1 to 5 only")

		








