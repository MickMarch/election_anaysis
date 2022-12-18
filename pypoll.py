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

# Initialize vote counter
total_votes = 0

# Candidate Options
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_votes = 0
winning_percentage = 0


# Open the election results and read the file
with open(file_to_load, "r") as election_data:
    file_reader = csv.reader(election_data)

    # Return and remove header row
    headers = next(file_reader)
    print(headers)

    for row in file_reader:

        # Increase total votes
        total_votes += 1

        # Get Candidate name
        candidate_name = row[2]

        # Add candidate to candidate options if not present
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        # Count each candidate vote
        candidate_votes[candidate_name] += 1

# Iterate through candidate list
for candidate_name in candidate_votes:

    # Retrieve votes of candidate
    votes = candidate_votes[candidate_name]

    # Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # Print the candidate's stats
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Record the winning stats
    if votes > winning_votes and vote_percentage > winning_percentage:
        winning_votes = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

# Create the Winning Candidate Summary
winning_candidate_summary = (
    f"-----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_votes:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------------"
)

print(winning_candidate_summary)
