import math

radius : float = float(input("Please, input a radius of the circle[m]\n")) #input

length : float = 2 * math.pi * radius #calculate the length
square : float = math.pi * (radius ** 2) #calculate the square

print(radius) #print input
print("Circle properties are:\n")
print("Length: {} metres".format(length)) # print length of the circle
print("Square: {} metres^2".format(square)) # print square of the circle


