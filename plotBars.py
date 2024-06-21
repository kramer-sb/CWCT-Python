# Function to plot bar graphs

def plotBars(data_list, plotsymbol):
    for i in range(40):  # use a for loop to print 40 blank lines and 
        print() # this "clears" out the console window
        # for each value in the list:
    for each_item in data_list:
        print(plotsymbol * each_item) # print "value" number of plotsymbols using string replication
    print() 

# Main Program
theList = [15, 10, 15, 20, 15, 30, 15, 40, 15, 50] # Build a list of numbers between 1 and 50
plotBars(theList, "*") 
print("The data is:", theList) 

print("End of program")
