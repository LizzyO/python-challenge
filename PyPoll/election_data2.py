import os
import csv

# Path to collect data from folder
poll_csv = os.path.join('election_data.csv')
# set path for file
with open(poll_csv) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #adding rows that start at 0
    total_votes = 0
    #create lists
    candidate_list= []
    vote_list = []
    #create dictionaries
    vote_count = {}
    vote_percent = {}
    #last find the winner
    winner = ""
    #skip the first row
    csv_header = next(csvreader)

 #loop through 
    for row in csvreader:
        #if candidate not yet then place it in a list for candidates
        if row[2] not in candidate_list:
            #create list for candidates
            candidate_list.append(row[2])
        #create list of all votes    
        vote_list.append(row[2])

    #then in the lists created 
    for row in candidate_list:
        #loop through names check the vote list count
        vote_count[row] = vote_list.count(row)
        #need total votes in order to get percent    
        total_votes+= vote_list.count(row)
        #once you get total votes get the vote percent
        for row in candidate_list:
            vote_percent[row]= round(vote_list.count(row)/total_votes*100,3)

    #Print out the voters name and their percentage stats
    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes {total_votes}')
    print(f'-------------------------')
    print(f'{vote_percent}: ({vote_count})')

