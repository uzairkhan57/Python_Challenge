# we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

# Set path for file
csvpath = PyBankcsv = os.path.join('Resources','budget_data.csv')


# Open and read the CSV
with open(csvpath, newline="") as csvfile:
    
    
    # Read header row
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
 
    # Declare variables
    months = []
    ProfitnLoss = []
    difference = []
    Increase_in_Date = []
    Decrease_in_Date = []
    
    # Count total number of months
    for row in csvreader:
        months.append(row[0])   
        ProfitnLoss.append(int(row[1]))
      
    
    # Print Statements
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months: ", len(months))
    print("Net Total: $", sum(ProfitnLoss))

    for i in range(1, len(ProfitnLoss)):
        
        #Average change between months
        difference.append(ProfitnLoss[i] - ProfitnLoss[i-1])
        
        #Average of values
        Average_Change = sum(difference) / len(difference)
        
        #Increase in date
        greatest_increase = max(difference)
        Increase_in_Date = str(months[difference.index(max(difference))])
        
        
        # decrease in dates
        greatest_decrease = min(difference)
        Decrease_in_Date = str(months[difference.index(min(difference))])
        
    # Print Statements
    print("Average Change: $", round(Average_Change))  
    print("Greatest Increase: ", Increase_in_Date, "($", greatest_increase,")")
    print("Greatest Decrease: ", Decrease_in_Date , "($", greatest_decrease,")")
 