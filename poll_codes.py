import os
import csv

#CSV Path

csvpath = Pypollcsv = os.path.join('Resources','election_data.csv')

# Open and read the CSV
with open(csvpath, newline="") as csvfile:

    
    # header
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
 
    #Declaring variables
    contestants = {}
    counts = 0
    casted_votes = 0
    votes_percentage = 0
    highest_votes = 0
    highest_voted = ""
    

    
    for row in csvreader:
        
        # Counting the Total Number of votes casted
        contestant = row[2]
        counts += 1
        if contestant in contestants.keys():
            contestants[contestant] += 1
        else:
            contestants[contestant] = 1
       
    
    
    # PrintING Statements
    print("Election Final Results")
    print("-------------------------------")
    print(f"Total Votes: {counts}")
    print("-------------------------------")
    
            
    #total number of votes
    for contestant in contestants:
        casted_votes += contestants[contestant]
    
        # percentage of votes
        votes_percentage = (contestants[contestant])/(counts) * 100
        print(f"{contestant}: {int(votes_percentage)}% {casted_votes}")
        
        if contestants[contestant] > highest_votes:
            highest_voted = contestant
            highest_votes= contestants[contestant]
        
        
    
    # The winner of the election
    print("-------------------------------")
    
    print(f"Winner: {highest_voted}")
    
    print("-------------------------------")



