# In this project, our final Python script will need to be able to deliver the following information when the script is run:

# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote
# -------------------------------------------------------------
# Import dependencies
import os
import csv

# Assign a variable to use for the file to load from a path
file_to_load = os.path.join("resources", "election_results.csv")

# Assign a variable to use for the file to save to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load, "r") as election_data:
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file
    headers = next(file_reader)
    print(headers)
