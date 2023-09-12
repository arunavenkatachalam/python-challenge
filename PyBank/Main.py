# Dependencies
import os
import csv

# Specify the file path
PyBank_csv ="PyBank\\Resources\\budget_data.csv"

# Open the file with default encoding 'UTF-8'.Specify the variable to hold the contents
with open(PyBank_csv,encoding='UTF-8') as csvfile:
    
# Create empty list to store the values of each column respectively    
    Date=[]
    Amount=[]
    Monthly_Change=[]

#  Specify the delimiter to read the file 
    csvreader=csv.reader(csvfile,delimiter=',')

    # Store the header using the variable csvheader
    csvheader=next(csvreader)

    # create a variable to store the values 
    count=0
    Total_Amount=0
    Total_Change=0
    Count_Change=0

    # Loop and store the data of row[0] and  row[1] in to Date and Amount list respectively
    for row in csvreader:
         Date.append(row[0])
         Amount.append(row[1])
         # Count the rows to calculate the Total months
         count = count+1 
         # Add the amount in each index and store the net total amount in the Total_Amount varaiable
         Total_Amount += int(row[1])
         

    # Loop through the range of Amount and calculate the monthly change and store the data in the Monthly_Change list
    for i in range(1,len(Amount)):
         change = int(Amount[i]) - int(Amount[i-1])
         Monthly_Change.append(change)
         # Using max and min function identify the maximum and minimum profit
         Increase_Profit = max(Monthly_Change)
         Decrease_Profit = min(Monthly_Change)
         
# print the calculated values as specified in the challenge 
print(f"Financial Analysis")
print("--------------------------------------------------------------")
print(f"Total months: {count}")
print(f"Net Total Amount: ${Total_Amount}")

# Loop through Monthly change to calculate the Total of monthly change
for i in Monthly_Change:
     Total_Change += int(i)
     Count_Change = Count_Change+1
# Calculate the Average change using the formula and print the same   
Average_Change = round(Total_Change/Count_Change,2)
print(f"Average change: ${Average_Change}") 

# Loop through the monthly change and based on the condition print both
# Greatest increase date and Amount
# Greatest Decrease date and Amount
for i in range(len(Monthly_Change)):
           if (Monthly_Change[i] == max(Monthly_Change)):
               Greatest_Increase_Date = Date[i+1]
               print(f"Greatest Increase in Profits: {Date[i+1]} ({Increase_Profit})")

           if (Monthly_Change[i] == min(Monthly_Change)):
               Greatest_Decrease_Date = Date[i+1]
               print(f"Greatest Decrease in Profits: {Date[i+1 ]} ({Decrease_Profit})")

# create a text file to store the result
Output_Path = "PyBank\\Analysis\\FinalResult_PyBank.txt"
# Open the file using "write" mode. Specify the variable to hold the contents
with open(Output_Path,'w') as textfile:
     # write the result in a text file
     textfile.write(f"Financial Analysis \n")
     textfile.write("-------------------------------------------------------------- \n")
     textfile.write(f"Total months: {count} \n")
     textfile.write(f"Net Total Amount: ${Total_Amount} \n")
     textfile.write(f"Average change: ${Average_Change} \n")
     textfile.write(f"Greatest Increase in Profits: {Greatest_Increase_Date} ({Increase_Profit}) \n")  
     textfile.write(f"Greatest Decrease in Profits: {Greatest_Decrease_Date} ({Decrease_Profit}) \n")
textfile.close()
     
