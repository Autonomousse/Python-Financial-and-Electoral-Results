# python-challenge
Analyzing financial and election data using Python.

## PyBank
### Goal
The goal of the PyBank assignment is to take financial data in a CSV file and analyze it using Python. There are two columns labelled `Date`and `Profit/Losses` that respectfully hold the month/year and the profit/loss.

The task involves creating a Python script that analyzes the data to calculate each of the following:

  - The total number of months included in the dataset

  - The net total amount of "Profit/Losses" over the entire period

  - The average of the changes in "Profit/Losses" over the entire period

  - The greatest increase in profits (date and amount) over the entire period

  - The greatest decrease in profits (date and amount) over the entire period

### Results
The output should appear as follows in the terminal and a text file should be exported with the results as well:

```
Financial Analysis 
-------------------------------------------------------- 
Total Months: 86 
Total: $38,382,578 
Average Change: $-2,315.12 
Greatest Increase in Profits: Feb-2012 ($1,926,159) 
Greatest Decrease in Profits: Sep-2013 ($-2,196,167)
```
## PyPoll
### Goal
The goal of the PyPoll assignment is similar in nature to the PyBank challenge above. We are given a CSV file with three columns labelled `Voter ID`, `County`, and `Candidate`. Create a Python script that analyzes the votes and calculates the following:

  - The total number of votes cast

  - A complete list of candidates who received votes

  - The percentage of votes each candidate won

  - The total number of votes each candidate won

  - The winner of the election based on popular vote.

### Results
The output should appear as follows in the terminal and a text file should be exported with the results as well:

```
Election Results 
---------------------------- 
Total Votes: 3,521,001 
---------------------------- 
Khan: 63.000% (2,218,231) 
Correy: 20.000% (704,200) 
Li: 14.000% (492,940) 
O'Tooley: 3.000% (105,630) 
---------------------------- 
Winner: Khan 
----------------------------
```
