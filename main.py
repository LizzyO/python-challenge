import os
import csv

# Path to collect data from folder
csvpath = os.path.join('budgetdata.csv')

# set path for file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.DictReader(csvfile, delimiter=',')
    month_count = 0
    net_total_amount = sum(float(row['Profit/Losses']) for row in csvreader)
    #loop through counting the months
    for row in csvreader:
        month_count += 1
    print(f'Total Months: {month_count}')
    print (f"Total: {net_total_amount}")