#acts a user interface that allows user will save data to a file. 
print("\nWelcome to the Journal Manager Program")
print("-" * 38)

def list_entries():
    print("-------------------------")
    with open("journal.txt", "r") as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            print(f"{index +1} {line.strip()}")
    print("-------------------------")

def create_entry():
    new_entry_text = input("\nEnter the text for the new journal entry: ")
    with open("journal.txt", "a") as file:
        file.write(new_entry_text + "\n")   

def view_entry():
    entry_to_view = int(input("\nEnter the line number of the entry you would like to view: "))
    with open("journal.txt", "r") as file:
        lines = file.readlines()
        print(lines[entry_to_view - 1])

def delete_entry():
    entry_to_delete = int(input("\nEnter the line number of the entry you would like to delete: "))
    with open("journal.txt", "r") as file:
        lines = file.readlines()
        del lines[entry_to_delete - 1]
        with open("journal.txt", "w") as file:
            file.writelines(lines)

while True:
    print("1. List entries")
    print("2. Create a new entry")
    print("3. View a specific entry")
    print("4. Delete entry")
    print("5. End the program")
    selected_command = input("\nWhat would you like to do? ")
    if selected_command == "1":
        list_entries()
    elif selected_command == "2":
        create_entry()
    elif selected_command == "3":
        view_entry()
    elif selected_command == "4":
        delete_entry()
    elif selected_command == "5":
        print("\nThank you for using the Journal Manager Program.\nHave a nice day!")
        print("\nEnd of program")
        break
    else: 
        print("\nThat is not a valid selection. Please enter a number from 1 through 5")
