name = input("Enter flower name: ")

if name == "Daisy": #if the input equals Daisy, we get the below print
    print("Yes - Daisy is the best plant ever!")
elif name == "daisy": #if the input is Daisy and is not capitalized, we get the below print
    print("No, I want a big Daisy!")
else: #if any other plant besides Daisy or daisy is chose, we get the below print
    print("Daisy! Not", name + "!")
