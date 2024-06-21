#  Purpose: Calculate Distance Traveled

Speed = 0 # validation to not allow anything zero or below
while Speed <= 0:
    Speed = int(input("Please enter the speed in MPH: "))
    if Speed <= 0:
        print("Input is invalid - must be greater than 0.")
Time = 0 # this is validation that time must be above 1 hour
while Time <= 1:
    Time = int(input("Please enter the number of hours traveled: "))
    if Time <= 1:
        print("Input is invalid - must be greater than 1 mph.")
    print()
    print("What is the speed in mph? ",Speed, "mph")
    print("How many hours  traveled? ",Time, "hours")
    print()

print('{:^15}{:^20}'.format("Hour", "Distance Traveled")) 
print("-" * 35)

# This where I begin a for loop, I think?
for t in range(Time):
    Distance = Speed * (t + 1)
    print('{:^15}{:^20}'.format(t + 1, Distance))
    
# for d in range(Distance): we need to add distance but I'm not sure how. 
# it's distance traveled divided by time but then added to one another
#     print(Distance)

print("\nThe distance traveled = ", Distance,"miles")
print()

print()
print("End of Program")
print()
