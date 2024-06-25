import random

#Dice Simulator
print("\nWelcome to the Dice Simulator!")
one = """
+-------+
|       |
|   •   |
|       |
+-------+
"""

two = """
+-------+
|  •    |
|       |
|    •  |
+-------+
"""

three = """
+-------+
|  •    |
|   •   |
|    •  |
+-------+
"""

four = """
+-------+
| •   • |
|       |
| •   • |
+-------+
"""

five = """
+-------+
| •   • |
|   •   |
| •   • |
+-------+
"""

six = """
+-------+
| •   • |
| •   • |
| •   • |
+-------+
"""
user_wants_to_exit = False

while not user_wants_to_exit:
    how_many_dice = int(input("\nHow many dice would you like to roll? (Enter -1 to exit): "))

    if how_many_dice == -1:
        user_wants_to_exit = True
        print("\nThanks for playing!")
    else: 
        die_faces = [one, two, three, four, five, six]
    
        for i in range(how_many_dice):
            selected_number = random.randint(1, 6)
            print(die_faces[selected_number - 1])

print("\nEnd of Program")
