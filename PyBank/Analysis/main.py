#import and create path link
import os
import csv
csvpath = os.path.join("..","Resources", "pyBanks_budget_data.csv")

    #define the variables
    # def Finacial_Analysis(Finance_data):
    #     Date = str(Finance_Data[0])
    #     profit_loss = int(Finance_data[1])

    

    #Print Finacial variable 


    #1. Count the lines within the csv

    #2. sum the entire profit_loss column to find total.

    #3. activate writer and add "change" column in csv

    #take row 2 from row 1 to determine "change"

    #find average of new change column to create a "average change"

    #open and read csv file
with open(csvpath) as csvfile:
      
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    print (f"CSV header: {header}")
    row_count = sum(1 for row in csvreader)
    print(f"Total Months: {row_count}")
    
    profit_loss =0
    for row in csvreader:
        profit_loss = profit_loss + float(row[1])
    print(profit_loss)