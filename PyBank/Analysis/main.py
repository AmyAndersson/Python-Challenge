import os
import csv

#create path
csvpath = os.path.join("..","Resources", "pyBanks_budget_data.csv")

#open and read csv file
with open(csvpath) as csvfile:
   
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print (f"CSV header: {csv_header}")

    """ for row in csvreader:
        print(row) """
    sum(1 for line in csvreader)
    #print("Total months" str(sum(1 for line in csvreader)))
    sum

