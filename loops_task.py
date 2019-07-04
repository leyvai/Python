
item = ""
total = 0
lista = []

while item != "done":
	item = input("Enter Item: ")
	if item == "done":
		break
	quantity = input("Enter quantity: ")
	price = float(input("Enter Price "))
	cart = float(price) * float(quantity)
	total = float(total) + float(cart)
	batch = {
	"item" : item,
	"price" : float(price),
	"quantity" : float(quantity),
	}
	lista.append (batch)

print ("---------------")
print ("receipt")
print ("---------------")
for x in lista:
	print (str(x["quantity"]) + " " + x["item"] + " " + str(x["price"]) + " KD")

print ("---------------")
print ("Total: %d KD" % (total) )

