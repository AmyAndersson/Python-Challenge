#import and create path link

import os

import csv

 

PyPollpath = os.path.join("..","Resources", "PyPoll_election_data.csv")

 

with open(PyPollpath) as csvfile:

    PyPollcsv = csv.reader(csvfile, delimiter="," )

    header = next(PyPollcsv)

    print(header)

    candidate_list=[]
    

    for row in PyPollcsv:
        candidate_list.append(row[2])
        #Khan_count = candidate_list.count("Khan")
    print(len(candidate_list))
    candidates = set(candidate_list)
    print(len(candidates))
    print(candidates)
    print(Khan_count)
    
          
        #if row[2] not in candidate:
            #candidate.append(row[2])
        #print(len(candidate))
        #candidate_list.append(row[2])
        #[canidate_list.append(x) for x in canidates if x not in canidate_list]
    #candidate_list= list(set(candidate_list))
    #print(candidate_list)
    #print(candidate_list)

    

 

    #count canidate names

 

#canidates.count(canidate name)

        #print(canidate_list)