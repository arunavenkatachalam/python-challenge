# Dependencies
import os
import csv

# Specify the file path
PyPoll_csv = "PyPoll\\Resources\\election_data.csv"

# Open the file with default encoding 'UTF-8'.Specify the variable to hold the contents
with open(PyPoll_csv,encoding='UTF-8') as csvfile:

    # Create empty list to store the values of each column respectively  
    BalletId = []
    County = []
    Candidate = []
    #  Specify the delimiter to read the file 
    csvreader=csv.reader(csvfile,delimiter=',')
    # Store the header using the variable csvheader
    csvheader=next(csvreader)

    # create a variable to store the values 
    count = 0
    candidate1_vote_Count = 0
    candidate2_vote_Count = 0
    candidate3_vote_Count = 0
    candidate1 = "Charles Casper Stockham"
    candidate2 = "Diana DeGette"
    candidate3 = "Raymon Anthony Doane"

# Loop and store the data of row[0],row[1] and row[2] in to BalletId, County and Candidate list respectively
    for row in csvreader:
        BalletId.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
        count = count + 1

# print the Election results and Total vote as specified in the challenge
    print("Election Results")
    print("-----------------------------------------------------------------------------")
    print(f"Total Votes: {count}")
    print("-----------------------------------------------------------------------------")

    # Loop through the candidate to count and store the number of votes each candidate received 
    for i in range(len(Candidate)):
        if (Candidate[i] == candidate1):
            candidate1_vote_Count += 1 
            
        if (Candidate[i] == candidate2):
            candidate2_vote_Count += 1 
            
        if (Candidate[i] == candidate3):
            candidate3_vote_Count += 1 
    # Calculate the percentage of vote each candidate won and print the same along with the candidate name and number of votes         
    Vote_Percentage_Candidate1 =  round(int(candidate1_vote_Count) / int(count) *100,3)
    Vote_Percentage_Candidate2 =  round(int(candidate2_vote_Count) / int(count) *100,3)
    Vote_Percentage_Candidate3 =  round(int(candidate3_vote_Count) / int(count) *100,3)
    print(f"{candidate1}: {Vote_Percentage_Candidate1 }% ({candidate1_vote_Count})")        
    print(f"{candidate2}: {Vote_Percentage_Candidate2 }% ({candidate2_vote_Count})")
    print(f"{candidate3}: {Vote_Percentage_Candidate3 }% ({candidate3_vote_Count})")
    print("-----------------------------------------------------------------------------")          
    
# create a dictionary to store the Candidate names as key and Vote percentage as value
    percentage_dict = {
    'Charles Casper Stockham': Vote_Percentage_Candidate1,
    'Diana DeGette': Vote_Percentage_Candidate2,
    'Raymon Anthony Doane': Vote_Percentage_Candidate3
}
    
    # identify the candidate with maximum vote and store the candidate name (Key) using the variable Winner
    Winner = max(percentage_dict,key=percentage_dict.get)

# Print the wining candidate name
    print(f"The Winner is: {Winner}")
print("-----------------------------------------------------------------------------")

# Specify the file to write to
Output_Path = "PyPoll\\Analysis\\FinalResult_PyPoll.txt"
# Open the file using "write" mode. Specify the variable to hold the contents
with open(Output_Path,'w') as textfile:
     # write the result in a text file
    textfile.write("Election Results \n")
    textfile.write("----------------------------------------------------------------------------- \n")
    textfile.write(f"Total Votes: {count} \n")
    textfile.write("----------------------------------------------------------------------------- \n")
    textfile.write(f"{candidate1}: {Vote_Percentage_Candidate1 }% ({candidate1_vote_Count}) \n")        
    textfile.write(f"{candidate2}: {Vote_Percentage_Candidate2 }% ({candidate2_vote_Count}) \n")
    textfile.write(f"{candidate3}: {Vote_Percentage_Candidate3 }% ({candidate3_vote_Count}) \n")
    textfile.write("----------------------------------------------------------------------------- \n")          
    textfile.write(f"The Winner is: {Winner} \n")
    textfile.write("----------------------------------------------------------------------------- \n")
textfile.close()