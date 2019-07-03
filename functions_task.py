import datetime

year = int(input ("Enter year of birth: "))
month = int(input ("Enter month of birth: "))
day = int(input ("Enter day of birth: "))
bday = datetime.date(int(year),int(month),int(day))
today = datetime.datetime.today()
todate = today.date()

def check_birthday():
	if todate < bday:
		return False
	else:
		return True

def calculate_age():
	result = todate - bday
	result = result.days
	year = result / 365
	result = result % 365
	month = result / 30
	days = result %30
	
	#old code (bad print method)
	# print ("You are " + str(int(year)) + " years, " + str(int(month)) + " months, and " + str(int(days)) + " days old")
	print ("You are %d years, %d months, and %d days old" % (year, month, days)) 

if check_birthday():
	calculate_age()
else:
	print ("\nWe do not work with people from the future")

