#PyBank, main.py
#print to terminal and with a *.txt file
#Total Months, Total, Average Change, Greatest Increase in Profits, Greatest Decrease in Profits

#importing os and csv modules
import os
import csv

#Path test
#dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)   

#import "Resources/budget_data.csv", same structure for GitHub
#make sure current directory correct for test filepath and eventual GitHub location

csvpath = os.path.join('Resources', 'budget_data.csv')
#/c/Users/jeffr/Desktop/PyBank/Resources

#test csvpath accuracy
#print(csvpath)
#verified correct

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)
    
    total = 0 

    for row in csvreader:
        total += int(row[1,1:86])
        #print(row), displays all entries for all columns

print(total)

# print("Financial Analysis")
# print("------")
# print(f"Total Months: {Total_Months}")
# print(f"Total: {Sum}")
# print(f"Average Change: {Average_Change}")
# print(f"Greatest Increase in Profits {Greatest_Profit}")
# print(f"Greatest Decrease in Profits {Greatest_Loss}")

#Use Sum for Total, Len for Total Months, Avg is Avg or Sum(list)/Len(list)








