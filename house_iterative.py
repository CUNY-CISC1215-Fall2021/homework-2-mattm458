sqft = 0
rooms = int(input("How many rooms are in your house? "))

for i in range(rooms):
    w = int(input("Width of room " + str(i+1) + ": "))
    l = int(input("Length of room " + str(i+1) + ": "))
    sqft = sqft + (w * l)

print("Your home is " + str(sqft) + " square feet")