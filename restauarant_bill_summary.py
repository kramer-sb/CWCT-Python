#Restaurant Bill Calculator:
mealCost = float(input("\nHow much did your meal cost?  ")) #promt user for amount of meal
tax = float(.0675 * mealCost) #compute tax of 6.75% for the meal
mealWithTax=float(mealCost + tax) 
tip = float(input("What percent will you tip? We suggest 18 percent: "))#prompt user for tip amount
tipConvert = float(tip/100) #convert to decimal
tipValue = float(tipConvert*mealCost)
#print("the tipValue is: ",tipValue)
grandTotal = mealWithTax + tipValue
print("\nRestaurant Bill Summary")
print("*" * 25)
print("Your meal cost:",format(mealCost,".2f"))#display: meal cost, tax amount, tip amount, total bill
print("The total tax on your meal:",format(tax,".2f"))
print("Your tip is:",format(tipValue,".2f"))
print("The grand total cost of your meal is:",format(grandTotal,".2f"))
print("\nEnd of program")
