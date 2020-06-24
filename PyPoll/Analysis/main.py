#import and create path link

import os

import csv

 

PyPollpath = os.path.join("..","Resources", "PyPoll_election_data.csv")

 

with open(PyPollpath) as csvfile:

    PyPollcsv = csv.reader(csvfile, delimiter="," )

    header = next(PyPollcsv)

    print(header)

    row_count = sum(1 for row in PyPollcsv)

    print(row_count)   

 

    canidates=[] 

    canidate_list = []

 

    for rows in PyPollcsv:

        canidates.append(row[2])

        #remove duplicates from list

    canidates_list = list(set(canidates))

        #[canidate_list.append(x) for x in canidates if x not in canidate_list]

    print(canidates_list)

    

 

    #count canidate names

 

#canidates.count(canidate name)

        #print(canidate_list)