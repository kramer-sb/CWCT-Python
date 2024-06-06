print(2+2)
# spaces improve readability
# 2 asterisks indicate exponents
# when both arguments are integers, the result is an integer, too
# when at least one argument is a float, the result is a float, too
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
# these will all be floats - do not follow the float rule as in multiplication
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
# use for division when you want an integer. 
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
# printing the remainder / modulo
print(14 % 4)
# beware of rounding
print(12 % 4.5)
# modulo uses left-sided binding
print(9 % 6 % 2)
# exponentation uses right-sided binding
print(2 ** 2 ** 3)
