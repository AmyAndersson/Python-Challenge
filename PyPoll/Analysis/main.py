#import and create path link

import os

import csv

 

PyPollpath = os.path.join("..","Resources", "PyPoll_election_data.csv")

 

with open(PyPollpath) as csvfile:

    PyPollcsv = csv.reader(csvfile, delimiter="," )

    header = next(PyPollcsv)

    print(header)

    candidate_list=[]
    total_votes =0
    Khan_count=0
    Correy_count=0
    Li_count=0
    OTooley_count=0
    
    for row in PyPollcsv:
        total_votes = total_votes +1
        candidate_list.append(row[2])
        if row[2] == "Khan":
            Khan_count = Khan_count +1
        if row[2] == "Correy":
            Correy_count = Correy_count +1
        if row[2] == "Li":
            Li_count = Li_count +1
        if row[2] == "O'Tooley":
            OTooley_count = OTooley_count +1
    
    #print(len(candidate_list))
    candidates = set(candidate_list)
    #print(len(candidates))
    #print(candidates)
    #print(Khan_count)
    Kahn_percent = round(((Khan_count / total_votes)*100),2)
    Correy_percent = round(((Correy_count / total_votes)*100),2)    
    Li_percent = round(((Li_count / total_votes)*100),2)      
    OTooley_percent = round(((OTooley_count / total_votes)*100),2)  
        
    if Kahn_percent > Correy_percent and Li_percent and OTooley_percent:
        winner= "Khan"
    if Correy_percent > Kahn_percent and Li_percent and OTooley_percent:
        winner= "Correy"
    if Li_percent > Correy_percent and Kahn_percent and OTooley_percent:
        winner= "Li"
    if OTooley_percent > Correy_percent and Li_percent and Kahn_percent:
        winner= "OTooley"
    
    print("Election Results")
    print("-----------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------")
    print(f"Khan: {Kahn_percent}% ({Khan_count})")
    print(f"Correy: {Correy_percent}% ({Correy_count})")
    print(f"Li: {Li_percent}% ({Li_count})")
    print(f"Khan: {Li_percent}% ({Li_count})")
    print("--------------------")
    print(f"Winner: {winner}")
    
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