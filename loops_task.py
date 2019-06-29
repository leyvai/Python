
item = ""
total = 0
lista = []

while item != "done":
	item = raw_input("Enter Item: ")
	if item == "done":
		break
	quantity = raw_input("Enter quantity: ")
	price = raw_input("Enter Price ")
	cart = int(price) * int(quantity)
	total = int(total) + cart 
	batch = {
	"item" : item,
	"price" : int(price),
	"quantity" : int(quantity),
	}
	lista.append (batch)

print "---------------"
print "receipt"
print "---------------"
for x in lista:
	print str(x["quantity"]) + " " + x["item"] + " " + str(x["price"]) + "KD"

print "---------------"
print "total: " + str(total)

