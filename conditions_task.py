n_one = raw_input("Enter a number ")
n_two = raw_input("Enter a second number ")
result = 0

operation = raw_input("Choose the operation: (+, -, /, *): ")

if n_one.isdigit() and n_two.isdigit():
 	if operation == "+":
		result = int(n_one)+ int(n_two)
		print result
	elif operation == "-":
		result = int(n_one) - int(n_two)
		print result
	elif operation == "/":
		result = int(n_one) / int(n_two)
		print result
	elif operation == "*":
		result = int(n_one) * int(n_two)
		print result
else:
	print ("Invalid Entry")	
	


