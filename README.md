# An Election Analysis

## Overview of Project

### Purpose

The purpose of this project was to write a Python script to analyze data from a .csv file containing election voter data. The script prints the results to the terminal and saves the results to a .txt file. 

### Code Functionality

The Python script will read the .csv file of ballot information and will determine the following:
- Total Votes
- Winning Candidate
- County With Highest Voter Turnout
- County Vote Count Breakdown
- Candidacountte Vote Count Breakdown

# Results of Election

## Outcomes
- Total Vote Count: 369,711
- Highlights:
  - Winning Candidate: Diana DeGette
  - County With Highest Voter Turnout: Denver
- County Vote Count Breakdown (Descending Order):
  - **Denver: 82.8% (306,055 Vote Count)**
  - Jefferson: 10.5% (38,855 Vote Count)
  - Arapahoe: 6.7% (24,801 Vote Count)
- Candidate Vote Count Breakdown (Descending Order):
  - **Diana DeGette: 73.8% (272,892 Vote Count)**
  - Charles Casper Stockham: 23.0% (85,213 Vote Count)
  - Raymon Anthony Doane: 3.1% (11,606 Vote Count)


# Summary

## Application of Script

The script currently could be used to analyze election data that follows the same .csv column format of "Ballot ID", "County", "Candidate". This analysis only showed 3 candidates and 3 counties, but the script is versatile in its ability to expand based on the amount of candidates and counties present in the data set being analyzed.

## Making Changes for Versatility

This script could be modified in a few ways for elections that have different requirements of analysis. 


### Adding Majority/Minority Win Analysis to Results

If the analysis needed to declare whether a candidate won by majority vote, the results portion of the script could be modified as such:
```python3
majority_win = "Majority" if winning_percentage > 50.0 else "Minority"
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"Majority/Minority Win: {majority_win}\n"
    f"-------------------------\n"
)
```

### Adding More Points of Analysis

If the script needed to analyze another point, like the political parties that the candidates are part of, the code would need to have a few new variables to add to the code.

Just like the candidates and counties, we would need to create similar variables:
```python3
party_list = []
party_votes = {}
```

During the `for row in reader:` row iterations, we would need to create a variable that will store the party name, from whichever column it is in:

`party_name = row[3]`

We would then have to make a check if the party has been seen before, and if it hasn't, we will add it to the `party_list` list object and start a vote counter in the `party_votes` dictionary object:

```python3
political_party_name = row[3]

if party_name not in party_list:
    party_list.append(party_name)
    party_votes[party_name] = 0
```

Then we will need to add a simple +1 to votes counted **outside** of that if statement:
```python3
political_party_name = row[3]

if party_name not in party_list:
    party_list.append(party_name)
    party_votes[party_name] = 0

party_votes[party_name] += 1
```

**With only slight modifications to the script, functionality can be added for many new types of data points to track in different types of elections.**