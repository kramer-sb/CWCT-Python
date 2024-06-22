# a = 200
# b = 15

# if b > a:
#     print("b is greater and a")
# elif a == b:
#     print("a and b are equal")
# else: 
#     print ("a is greater than b")

# print("end of program")

#-------------------------

# i = 1

# while i <= 6:
#     print(i)
#     i = i + 1
#     if i == 3:
#         break

#-------------------------

# thislist = [1,5,7,9,3]    
# print(thislist)

#-------------------------

# for x in range(6):
#     x = x + 10
#     print(x)

#-------------------------

# for x in range (0, 12, 2):
#     print(x)

#-------------------------

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break

#-------------------------

# fruits = ["apple", "banana", "cherry"]

# print(fruits[1])

#-------------------------

# a = 4
# b = 3
# if a == 3 and b ==3:
#     print("everyone is equal")
# else: 
#     print("not all equal")

#-------------------------

# a = 4
# b = 9
# if a == 3 or b ==3:
#     print("someone is equal")
# else: 
#     print("no one is equal")

#-------------------------

#(1 * 8) + (1 * 4) + (1 * 2) + (0 * 1) = 14

#Initialize a list
# myList = ["apple", "banana", "cherry", "kiwi", "grape", "pear", "orange"]

# print(myList[-2:-0])

#--------------------

# SHALLOW COPY - doesn't take up memory in the stack.

# Bag1 = [1, 2, 3]
# Bag2 = Bag1 #here we set them equal to each other

# print("Bag1 =", Bag1) #so this prints what we expect
# print("Bag2 =", Bag2) #and we expect this to print the same because of line 3

# Bag1[0] = 1111

# print("Bag1 =", Bag1) 
# print("Bag2 =", Bag2) #shallow copy. when working with equality (=)
# # doesn't copy the list, but sets the memory address of bag 1 = bag 2. 
# # both pointing to the same location in memory. 
# # change one, and the other changes as well. 

# Bag2[1] = 2222

# print("Bag1 =", Bag1) #proving the point that changing bag 2 changes bag 1. 
# print("Bag2 =", Bag2)

# **** DEEP COPY **** uses the slice operator, the colon

# Bag1 = [1, 2, 3]
# #slice
# Bag2 = Bag1[:] #here we are telling python to copy the entire contents of Bag 1. This is a deep copy

# print("Bag1 =", Bag1)
# print("Bag2 =", Bag2)

# Bag1[0] = 1111 #here we are adding to Bag 1 - it will NOT affect bag 2.
# print("Bag1 =", Bag1)
# print("Bag2 =", Bag2)

#Here is what the above code prints:
# Bag1 = [1, 2, 3] 1st print statement
# Bag2 = [1, 2, 3] 2nd print statement
# Bag1 = [1111, 2, 3] 3rd print
# Bag2 = [1, 2, 3] 4th print



#very cool list within a list
# myList = [[1,2,3], [4,5,6], [7,8,9]]

# print(myList[1])
# print(myList[1][0])
