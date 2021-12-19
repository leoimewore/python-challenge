# First Access csv file

import csv
csv_path= (r"C:\Users\leoim\python-challenge\PyPoll\Resources\election_data.csv")

total_votes=0
candidates=[]
candidates_votes={}
winning_votes=0
winning_candidate= ""
with open(csv_path, 'r') as file:
   poll_data=csv.reader(file, delimiter=',')
   header=next(poll_data)


   for row in poll_data:
       total_votes+=1    #count total number of votes
       if row[2] not in candidates:    #Get unique values from the candidate column
           candidates.append(row[2])

           candidates_votes[row[2]]=0

       candidates_votes[row[2]]+=1


   for candidate in candidates_votes:
       votes=candidates_votes[candidate]
       votes_percent= (float(votes)/float(total_votes)) *100


       if votes> winning_votes:
           winning_votes= votes
           winning_candidate=candidate
       

       print(f'{candidate}:  {votes} votes {votes_percent} %')

print(candidates)

print(total_votes)
print(winning_candidate)
print(winning_votes)
      


          


          
  

  