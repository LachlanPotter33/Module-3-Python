import os

import csv

csv_path = os.path.join('Resources','budget_data.csv')
#Financial_Analysis = os.path.join('Financial_Analysis.txt')
csvpath = os.path.join('Resources','budget_data.csv')
with open(csv_path) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)
    csv_header = next(csv_reader)

    #Take total numer of months
    changes = []
    total_months = 0
    total_pl = 0 
    rows = []
    for row in csv_reader:
        
        total_months += 1
        total_pl += float(row[1])
        new_month = row[1]
        rows.append(row)
        
        if total_months > 1 :
            changes.append(float(new_month) - float(old_month))
        old_month = row[1]
    
    greatest_inc_value = max(changes)
    greatest_inc_index = changes.index(greatest_inc_value)
    greatest_inc_month = rows[greatest_inc_index+1][0]

    greatest_dec_value = min(changes)
    greatest_dec_index = changes.index(greatest_dec_value)
    greatest_dec_month = rows[greatest_dec_index+1][0]

    average_change = sum(changes)/len(changes)
    
    print("Financial_Analysis")
    print("Total Months: ", total_months)
    print(f"Total: ${total_pl:.0f}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_inc_month} ${greatest_inc_value:.0f}")
    print(f"Greatest Decrease in Profits: {greatest_dec_month} ${greatest_dec_value:.0f}")
    #Financial_Analysis = os.path.join('Financial_Analysis.txt')

file = open('Financial_Analysis.txt', 'w')
with open ("Financial_Analysis.txt", 'w') as txt_file :
    
    file.write("Financial Analysis\n"
              "----------------------------\n"
              "Total Months: , total_months\n"
               f"Total: ${total_pl:.0f}\n"
               f"Average Change: ${average_change:.2f}\n"
               f"Greatest Increase in Profits: {greatest_inc_month} ${greatest_inc_value:.0f}\n"
               f"Greatest Decrease in Profits: {greatest_dec_month} ${greatest_dec_value:.0f}")
    file.close()