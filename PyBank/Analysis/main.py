#import and create path link
import os
import csv

budgetpath = os.path.join("..","Resources", "PyBanks_budget_data.csv")
    
with open(budgetpath) as csvfile:
      
       #csv reader  
       Budget_csv = csv.reader(csvfile, delimiter=",")
       header = next(Budget_csv)

       #defining variables
       row_count = 0
       Total = 0
       TotalChange = 0
       PreviousTotal = 0
       MaxChange = 0
       MinChange = 0
       
       #create a for loop that runs through the dataset
       for row in Budget_csv:
           #determine the total sum of profits and loss
            Total = Total + int(row[1])
            #create an if statement for change (row 2 - row 1)
            if row_count == 0:
                change = int(row[1])
                PreviousTotal = change   
            else:
                change = int(row[1]) - PreviousTotal
                TotalChange = TotalChange + change
                PreviousTotal = int(row[1])
                #create an if statement to replace maxchange everytime a bigger value is found. Do same for min
                if change > MaxChange:
                    MaxChange = change
                    MaxDate = row[0]
                if change < MinChange:
                    MinChange = change
                    MinDate = row[0]
            #add 1 to row to count data points
            row_count = row_count + 1
#     #find the average change             
averageChange = (round(TotalChange / (row_count - 1),2))

print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {row_count}")
print(f"Total:{Total}")
print(f"Average Change: ${averageChange}")
print(f"Greatest increase in Profits on {MaxDate}: (${MaxChange})")
print(f"Greatest decrease in Profits on {MinDate}: (${MinChange})")
   

output_path = os.path.join("..", "Results", "Financial Analysis.csv")

with open(output_path, 'w', newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow([f"Total:{Total}"])
    csvwriter.writerow([f"Average Change: ${averageChange}"])
    csvwriter.writerow([f"Greatest increase in Profits on {MaxDate}: (${MaxChange})"])
    csvwriter.writerow([f"Greatest decrease in Profits on {MinDate}: (${MinChange})"])

   