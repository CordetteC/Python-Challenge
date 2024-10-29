# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
# Define lists and dictionaries to track candidate names and vote counts
total_votes = 0  # Track the total number of votes cast
candidate_list = [] 
percentage_won= {} #Dictionaries store data in key-value pairs, allowing you to associate each candidate's name (the key) with their corresponding vote count or percentage (the value). 
total_won= {} #Dictionaries can dynamically grow as you add new candidates. You don't need to worry about the order of candidates, making it easier to handle varying numbers of candidates.

# Winning Candidate and Winning Count Tracker
winning_count=0 # Variable to store the count of votes for the winning candidate
winner = ""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes+=1

        # Get the candidate's name from the row
        candidate=row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            total_won[candidate] = 0 #initialize the new candidates vote count
        total_won[candidate]+=1 #add the vote to their count

# Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_list:
        percentage_won[candidate]=(total_won[candidate]/total_votes)*100

        # Update the winning candidate if this one has more votes
        if total_won[candidate] > winning_count:
            winning_count = total_won[candidate] #this works because it assumes winning count is 0 when it runs for the first candidate b/c thats how we set the variable
            winner = candidate

     
    # Generate and print the winning candidate summary/election results
output_summary = (
    f"\nElection Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
)
for candidate in candidate_list:
    output_summary+= f"{candidate}: {percentage_won[candidate]:.3f}% ({total_won[candidate]})\n"
output_summary+= (   
    f"----------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------\n"
)

# Print the output summary
print(output_summary)
# Export the results to the specified output file
with open(file_to_output, 'w') as file:
    file.write(output_summary)

    # Save the winning candidate summary to the text file
