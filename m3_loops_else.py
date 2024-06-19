#this is twisted, but worth noting.

i = 111

#the first argument in range() determines the initial (first) value of the control variable (i).
#The last argument in range() shows the first value the control variable (i) will not be assigned

for i in range(2, 1):
    print(i)
else:
    print("else:", i) #the loop never runs so the else statement prints

#but this one makes more sense. we didn't assign i immediately. 

for i in range(5):
    print(i)
else:
    print("else:", i)
