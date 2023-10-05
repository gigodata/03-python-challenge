# main.py

# Script for PyPoll analysis using Python - Module 03 - MSU Data Analytics Bootcamp
# Result returned is a summary analysis of tally of votes by candidate, and % of total, and winner name
# Created: 2023-10-03
# Last Modified: 2023-10-05
# Author: Adrian Santos
# v1.0

# Notes: I worked on this part2 of the assignment using a similar methodology as I approached Part1
# I used the AI feature of Bing in order to understand what was wrong with my approach
# The AI modified the code that I had written so far, and included the pseudocode necessary to process the data in the CSV file
# It provided a helpful approach and provided assistance in the correct programming format to arrive at the desired output
# Several iterations were required to arrive at correct result
# I added additional formatting to include commas in figures, to allow for better readability

###############################################################

# Import functions and clear Terminal window
import csv
import os

# Clear screen so output is clean & fresh for output of results
os.system('clear')

file_name = "/Users/adrian/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv"
output_file = "election_results.txt"

# Create a dictionary to store the candidate names and their vote counts
candidate_votes = {}

# Open the CSV file as read-only
with open(file_name, "r") as csvfile:
    csvreader = csv.reader(csvfile)

    # Read the first row as the header names for this dataset
    csv_header = next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Get the candidate name from the current row
        candidate_name = row[2]

        # If the candidate name is not already in the dictionary, add it with a vote count of 1
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 1
        # If the candidate name is already in the dictionary, increment their vote count by 1
        else:
            candidate_votes[candidate_name] += 1

# Print out the total number of votes cast and each candidate's vote count
total_votes = sum(candidate_votes.values())
formatted_votes = "{:,}".format(total_votes)
output_lines = []
output_lines.append("\n")
output_lines.append("Election Results\n")
output_lines.append("-------------------------\n")
output_lines.append(f"Total Votes: {formatted_votes}\n")
output_lines.append("-------------------------\n")
for candidate, votes in candidate_votes.items():
    vote_pct = round(votes / total_votes * 100, 3)
    formatted_votes = "{:,}".format(votes)
    output_lines.append(f"{candidate}: {vote_pct}% {formatted_votes}\n")
output_lines.append("-------------------------\n")
winner = max(candidate_votes, key=candidate_votes.get)
output_lines.append(f"Winner: {winner}\n")
output_lines.append("-------------------------\n")

# Write the output lines to a text file and display them in the terminal
with open(output_file, "w") as f:
    f.writelines(output_lines)
    print("".join(output_lines))

# I removed the () around the tally of votes in the example provided in the exercise.
# Numbers in parentheses indicate negative numbers. Votes are positive values, so () around the figures erroneously implies a negative value.

# End of Script