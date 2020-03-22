import os
import csv

# Path to collect data from folder
csvpath = os.path.join('budgetdata.csv')

# set path for file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #setting variables for first row
    month_count = 1
    prev_amt = 1
    net_total_amount = 0
    #get difference in change values
    diff_change = 0
    av_change = 0
    #use diff change value to get max and min profits
    max_profit = 0
    min_profit = 0
    date = []
    #skip the first row
    csv_header = next(csvreader)
    #list for difference
    diff_list = []
      
    #loop through counting the months
    for row in csvreader:
        #for first interation
        if month_count == 1:
            prev_amt = int(row[1]) 
            month_count += 1
            net_total_amount = net_total_amount + int(row[1])
        #everything after first
        else:
            #subtract row from previous row in profit/losses
            diff_change = int(row[1]) - prev_amt
            prev_amt = int(row[1])
            #count each row after first row
            month_count += 1
            #first row with int is defined, then add each row in "profit/losses"
            net_total_amount = net_total_amount + int(row[1])    
            #create list each diff change and date
            diff_list.append(diff_change)
            date.append(row[0])
    #calculate using diff_list created
    av_change = sum(diff_list)/ (month_count -2)
    max_profit= max(diff_list)
    min_profit= min(diff_list)
    max_profit_date = date[diff_list.index(max_profit)]
    min_profit_date = date[diff_list.index(min_profit)]
   
    print(f'Total Months: {month_count - 1}')
    print (f'Total: ${net_total_amount}')
    print(f'Average Change: ${av_change}')
    print(f'Greatest Increase in Profits: {max_profit_date} (${max_profit})')
    print(f'Greatest Decrease in Profits: {min_profit_date} (${min_profit})')


# Specify the file to write to
output_path = os.path.join("..", "PyBank", "new.txt")

with open(output_path, 'w') as textfile:

    # Initialize csv.writer
    csvwriter = csv.writer(textfile, delimiter=',')

    # Write the first row 
    csvwriter.writerow(['Total Months: {month_count - 1}'])
    # Write the second row
    csvwriter.writerow(['Total: ${net_total_amount}'])
