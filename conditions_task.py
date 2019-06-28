n_one = raw_input("Enter a number ")
n_two = raw_input("Enter a second number ")
result = 0
nu_one = int(n_one)
nu_two = int(n_two)

operation = raw_input("Choose the operation: (+, -, /, *): ")

if nu_one != int(n_one) or nu_two != int(n_two):
	print ("Invalid Entry")
elif operation == "+":
		result = nu_one + nu_two
elif operation == "-":
		result = nu_one - nu_two
elif operation == "/":
		result = nu_one / nu_two
elif operation == "*":
		result = nu_one * nu_two

print result