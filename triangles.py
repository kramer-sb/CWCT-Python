# Triangles

print("Triangle Program")
# Input the side lengths
sideA = float(input("Side A? "))
sideB = float(input("Side B? "))
sideC = float(input("Side C? "))

# Validate the input - leave this for last

# Initialize some boolean flags
IsTriangle = False
IsRightTriangle = False
IsIsoscelesTriangle = False
IsEquilateralTriangle = False

# A triangle has three sides where the sum of the length of any (every) two 
# of the sides must exceed the other side.

# Do we have a triangle?
IsTriangle = (sideA + sideB > sideC) and (sideA + sideC > sideB) and (sideB + sideC > sideA)
if IsTriangle:
    print("Yes, we have a triangle!")
else:
    print("Sorry, no triangle today.")
    exit()

# Do we have a equilateral triangle?
# all sides must be equal
IsEquilateralTriangle = sideA == sideB == sideC
# In an isosceles triangle the length of any two of the sides must be equal.

# do we have an isoceles triangle?
# In an isosceles triangle the length of any two of the sides must be equal.
IsIsoscelesTriangle = (sideA == sideB) or (sideA == sideC) or (sideB == sideC)

# Do we have a right triangle?
# In a right triangle, the square of the length of the longest side is equal to
# the sum of the squares of the lengths of the other two sides.
IsRightTriangle = (sideA**2 + sideB**2 == sideC**2) or (sideA**2 + sideC**2 == sideB**2) or (sideB**2 + sideC**2 == sideA**2)

# print the results
if IsEquilateralTriangle:
    print("we have an EQUILATERAL triangle!")
elif IsIsoscelesTriangle:
    print("We have an ISOCELES triangle!")
else:
    print("We have a RIGHT triangle!")

print("end of program")
