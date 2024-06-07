print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))

var = 1
print(var)

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)
# can drop the + and use a comma instead and get the same result
var = "3.8.5"
print("Python version: " + var)
#question here is what is var going to print? 
var = 100
var = 200 + 300
print(var)
# use of the Pythagorean theorem
# please tell me I don't need high math, Lord
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

john = 3
mary = 5
adam = 6
total_apples = john + mary + adam

print('The total number of apples: ', total_apples)

#the exercise here was to fill in the second set of variables.
kilometers = 12.25
miles = 7.38

miles_to_kilometers = 7.38 * 1.61
kilometers_to_miles = 12.25 / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# 3x3 - 2x2 + 3x - 1
# x =  # hardcode your test data here. 
# using sample data of x = 0 and x = 1  and x = -1 
#x = float(x)
# write your code here
#print("y =", y)

x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

a = '1'
b = "1"
print(a + b)
# here's the input function
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

# Testing TypeError message.
# uncomment the next three lines to try it out, know that it errors
# anything = input("Enter a number: ")
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)


anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
