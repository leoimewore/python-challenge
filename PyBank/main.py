# First Access csv file

import csv
csv_path= (r"C:\Users\leoim\python-challenge\PyBank\Resources\budget_data.csv")


#Initialize counter for number months and total sum and create an empty net-change list
num_of_months=0       
total_sum=0
net_change_list=[]
month_of_change=[]

#open file 

with open(csv_path, 'r') as file:
   budget_csv =csv.reader(file, delimiter=',')
   header=next(budget_csv)
   
   # Pick the first data row from the csv file
   first_row=next(budget_csv)
   prev_row=int(first_row[1])




   # initialize with the first row to get accurate data
   total_sum+= prev_row
   num_of_months+=1



#Loop through the csv file
   
   for row in budget_csv:
       num_of_months+=1
       total_sum+= int(row[1])
       net_change=int(row[1])-prev_row
       prev_row= int(row[1])
       net_change_list.append(net_change)
       month_of_change+=[row[0]]


     # Net average for all profit and loss changes 
   net_change_avg=sum(net_change_list)/len(net_change_list) 
   

   #Greatest increase and decrease of profit/losses 
   great_increase=max(net_change_list)
   great_decrease=min(net_change_list)


   
       
       
       
       
       
       






       

       
       

       





 
  

       

   print(f'Total number of months: {num_of_months} months')
   print(f'Net total amount: ${total_sum}')
   print(f'Net Average change Profit/losses: ${net_change_avg}')
   print(f'Greatest increase in profit: ${great_increase}')
   print(f'Greatest decrease in profit: ${great_decrease}')
   

   
   
  

