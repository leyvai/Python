skills = ["Jumping", "Punching", "Crying", "Sobbing", "Running", "Snoozing"]
cv = {}
skill_count = 0

name = raw_input ("What is your name? ")
age = raw_input ("What is your age? ")
experience = raw_input ("How many years of experience do you have? ")

cv["name"] = name
cv["age"] = age
cv["experience"] = experience
cv["Skills"] = ""
cv["Skills2"] = ""

for x in skills:
	
	skill_count = skill_count + 1
	print str(skill_count) + "- " + x

skill1 = raw_input ("Please select from the above: ")
skill2 = raw_input ("Please select one more skill: ")

skill1 = int(skill1) - 1
skill2 = int(skill2) - 1

cv ["Skills"] = skills[skill1]
cv ["Skills2"] = skills[skill2]

if cv["Skills"] == "Snoozing" or cv["Skills2"] == "Snoozing":
	print "You love snoozing! You get to Pass!"
else:
	print "You are not lazy, therefore you Fail."


