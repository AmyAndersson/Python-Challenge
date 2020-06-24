#import and create path link
import os
import csv

budgetpath = os.path.join("..","Resources", "PyBanks_budget_data.csv")
    

    #1. Count the lines within the csv

    #2. sum the entire profit_loss column to find total.

    #3. activate writer and add "change" column in csv

    #take row 2 from row 1 to determine "change"

    #find average of new change column to create a "average change"

    #open and read csv file
with open(budgetpath) as csvfile:
      
        #1  
       Budget_csv = csv.reader(csvfile, delimiter=",")
       header = next(Budget_csv)
       #print (f"CSV header: {header}")
       row_count = 0
       Total = 0
       TotalChange = 0
       PreviousTotal = 0
       MaxChange = 0
       MinChange = 0

       for row in Budget_csv:
            Total = Total + int(row[1])
            if row_count == 0:
                change = int(row[1])
                PreviousTotal = change
            else:
                change = int(row[1]) - PreviousTotal
                TotalChange = TotalChange + change
                PreviousTotal = int(row[1])
                if change > MaxChange:
                    MaxChange = change
                    MaxDate = row[0]
                if change < MinChange:
                    MinChange = change
                    MinDate = row[0]



        
            row_count = row_count + 1

#totalchange = sum(change)
averageChange = TotalChange / (row_count - 1)

print(f"Total Months: {row_count}")
print(f"Total:{Total}")
print(f"Average Change: {averageChange}")
print(f"Greatest increase in Profits on {MaxDate}: {MaxChange}")
print(f"Greatest decrease in Profits on {MinDate}: {MinChange}")
    