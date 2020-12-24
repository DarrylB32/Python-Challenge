# Python-Financial_and_Election_Analysis
This folder has two scripts, one focusing on [Financial Records](Financial_Analysis/Main.py) and the other focusing on [Election Poll](Election Analysis/Main.py) data. 

### Financial Records
The [Financial Records](Financial_Analysis/Main.py) script reads in the [budget data](Financial_Analysis/Resources/budget_data.csv) for a fictitious company. 

The script calculates the:
* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The average of the changes in "Profit/Losses" over the entire period
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in losses (date and amount) over the entire period
```text
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
```
### Election Poll
The [Election Poll](Election_Analysis/Main.py) script reads in the [election data](Election_Analysis/Resources/election_data.csv) for a fictitious small town. 

The script calculates the:
* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote.
```text
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
```
### Tech Stack
* Python
* Jupter Notebook

### User Instructions
* Clone the repository: git clone https://github.com/DarrylB32/Python-Financial_and_Election_Analysis 
* Open and execute [Financial Analysis Main](Financial_Analysis/Main.py) file.
* Open and execute [Election Analysis Main](Election_Analysis/Main.py) file.
 
### Additional Notes
