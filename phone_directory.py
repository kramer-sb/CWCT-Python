import csv
def show_directory(phone_directory):
    print()
    for name in phone_dir:
        print(name, phone_directory[name], sep="\t")

def add_directory(phone_directory):
    print("Add to directory")
    name = input("Name: ")
    number = input("Number: ")
    phone_directory[name] = number

def update_directory(phone_directory):
    print("Edit directory")
    name = input("Name: ")
    number = input("New Number: ")
    if (name in phone_directory):
        phone_directory[name] = number
    else: 
        print(name, "not found")

def delete_directory(phone_directory):
    print("Delete directory entry")
    name = input("Name: ")
    if (name in phone_directory):
        del phone_directory[name]
    else: 
        print(name, "not found")        

# Function to read a CSV
def readCSV(csvFile):
    phone_dir = {}
    with open(csvFile, mode='r') as infile:
        reader = csv.reader(infile, delimiter=',')
        first_line = True
        for row in reader:
            if first_line:
        	    # Skip header row
                first_line = False
            else:
                phone_dir[row[0]] = row[1]
    return phone_dir

#Function to write a CSV
def writeCSV(csvFile, phone_dir, column1, column2):
    with open(csvFile, mode='w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter=',')
        writer.writerow([column1, column2])
        for item in phone_dir:
           writer.writerow([item, phone_dir[item]])

# ** MAIN PROGRAM **
print("\nWelcome to the Phone Directory Application")
print("-" * 42)

command = -1
csvfilename = "phone_dir.csv"
phone_dir = readCSV(csvfilename)

while command != 0:
    print("\nCommand Menu")
    print("1 - Show phone directory")
    print("2 - Add to phone directory")
    print("3 - Update phone directory")
    print("4 - Delete phone directory")
    print("0 - Exit\n")
    command = int(input("Enter the number of the command: "))
    if command == 1:
        show_directory(phone_dir)
    elif command == 2:
       add_directory(phone_dir)
       writeCSV(csvfilename,phone_dir, "name", "number")
       show_directory(phone_dir)
    elif command == 3:
        update_directory(phone_dir)
        writeCSV(csvfilename,phone_dir, "name", "number")
        show_directory(phone_dir)
    elif command == 4:
        delete_directory(phone_dir)
        writeCSV(csvfilename,phone_dir, "name", "number")
        show_directory(phone_dir)
print("\nEnd of program")
