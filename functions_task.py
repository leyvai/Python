import datetime

year = raw_input ("Enter year of birth: ")
month = raw_input ("Enter month of birth: ")
day = raw_input ("Enter day of birth: ")
bday = datetime.date(int(year),int(month),int(day))
today = datetime.datetime.today()
todate = today.date()

def check_birthday():
	if todate < bday:
		return False
	else:
		calculate_age()


def calculate_age():
	age_year = todate.year - bday.year
	age_month = todate.month - bday.month
	age_day = todate.day - bday.day
	

	print ("You are " + str(age_year) + " years, " + str(age_month) + " months, and " + str(age_day) + " days old")

check_birthday()

