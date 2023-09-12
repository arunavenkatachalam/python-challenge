# python challenge

# PyBank Analysis

1. Download the csv file budget_data.csv for PyBank analysis. File consist of two columns Date and Profit/Losses.

2. Create a Python script to perform the calculations. Start with importing the os and csv to read the csv file. 

3. Specify the file path and store the contents in the variable. Open the file with the encoding 'UTF-8' and store the contents in the variable, by default the file will be open in read mode.

4. Specify the delimiter in this file it is comma(,) to read the file. Store the header using the variable.

5. Create empty list to store the data of each column. Also create variables count, Total_Amount, Total_Change and Count_Change to store the Total months, Net total amount, Total monthly change and count of monthly change.
    
6. loop through the row in the file and append the data available in row[0] and row[1] in to Date and Amount list respectively. Calculate the number of rows and total amount.

7. Loop through the range of the Amount starting from index[1] as there would be no monthly change for the first month. Calculate the monthly change, count of monthly change and store this value in the Monthly_Change list and Count_Change variable. 

8. Using max and min function calculate the highest profit and lowest profit based on the monthly change and store this value with the variable Increase_Profit and Decrease_Profit.

9. Print the calculated value as specified in the challenge. Again loop through the monthly change to calculate the total monthly change.

10. Calculate the Average_Change using the formula Total_Change/Count_Change and round the values to two decimal places. print the average change.

11. print the greatest increase and greatest decrease in profits along with the date based on the condition.

12. Create a new text file and store all the result. Set the path where the file should be created and open the file in write mode. Write the result in the file and close the text file.
 


# PyPoll Analysis

1. Download the csv file election_data.csv for PyPoll Analysis. File consist of three columns BalletId, County and Candidate.

2. Create a Python script to perform the calculations. Start with importing os and csv to read the csv file. 

3. Specify the file path and store the contents in the variable. Open the file with the encoding 'UTF-8' and store the contents in the variable, by default the file will be open in read mode.

4. Specify the delimiter in this file it is comma(,) to read the file. Store the header using the variable.

5. Create empty list to store the data of each column. Also create variables count,candidate1_vote_Count, candidate2_vote_Count, candidate3_vote_Count to store the overall vote count and individual vote count of each candidate. Store the candidate name in seperate variables namely candidate1, candidate2 and candidate3.
    
6. Loop through the row in the file and append the data available in row[0], row[1] and row[2] in to BalletId, County and Candidate list respectively. Calculate the number of votes and store in count.

7. print the Election results and Total vote as specified in the challenge. Loop through the candidate to count and store the number of votes each candidate received based on the condition.

8. Calculate the percentage of vote each candidate won and round the values to three decimal places. Print the same along with the candidate name and number of votes.

9. Create a dictionary to store the Candidate names as key and Vote percentage as value. Identify the candidate with maximum vote and store the candidate name (Key) using the variable Winner. Print the winning candidate name.

10. Create a new text file and store all the result. Set the path where the file should be created and open the file in write mode. Write the result in the file and close the text file.