# # Values

# name = raw_input("What is your name? ")
# time = raw_input("What time was it? ")
# items = raw_input("Write an item: ")
# scream = raw_input("Tell me anything: ")
# action = raw_input("Descript a verb: ")

# print ("It was " + time + " o'clock when I heard a knock at the door. " +
# 	"I opened the door and there was a box full of " + items + " with a note saying 'From " + name.capitalize() + "'. " + 
# 	"Just as I closed the door I heard a scream '" + scream.upper() + "'. " +
# 	"I froze in place and all I could do was " + action + ".")

print ("Mad libs where libs get Mad")
print (" Start Below:")
print("")
time = input("Number: ")
items = input("Noun(plural): ")
name = input("Name: ")
scream = input("Sentence: ")
action = input("Verb: ")
print("")
print ("\tIt was %s o'clock when I heard a knock at the door." % (time))
print ("\tI opened the door and there was a box full of %s with a note saying \"From Mr. %s\"." % (items, name.capitalize()))
print ("\tJust as I closed the door I heard a scream \"%s\"." % (scream.upper()))
print ("\tI froze in place and all I could do was %s." % (action))

