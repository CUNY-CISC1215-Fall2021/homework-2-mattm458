sqft = 0
rooms = int(input("How many rooms are in your house? "))

def square_feet(i, total_rooms, sqft):
    if i > total_rooms:
        print("Your home is " + str(sqft) + " square feet")
    else:
        w = int(input("Width of room " + str(i) + ": "))
        l = int(input("Length of room " + str(i) + ": "))
        sqft = sqft + (w * l)
        square_feet(i+1, total_rooms, sqft)

square_feet(1, rooms, 0)