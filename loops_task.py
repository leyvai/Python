
item = ""
total = 0
lista = []

while item != "done":
	item = input("Enter Item: ")
	if item == "done":
		break
	quantity = input("Enter quantity: ")
	price = input("Enter Price ")
	cart = int(price) * int(quantity)
	total = int(total) + cart 
	batch = {
	"item" : item,
	"price" : int(price),
	"quantity" : int(quantity),
	}
	lista.append (batch)

print ("---------------")
print ("receipt")
print ("---------------")
for x in lista:
	print (str(x["quantity"]) + " " + x["item"] + " " + str(x["price"]) + "KD")

print ("---------------")
print ("Total: %dKD" % (total) )

