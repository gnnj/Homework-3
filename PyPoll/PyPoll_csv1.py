# Import modules
import csv
import os
import sys
from collections import Counter

# Create lists
voter_id = []
county = []
candidate = []
candidate_list = []
candidate_name = []
votes = []
percent_of_votes = []

# Open the CSV files
csv1 = os.path.join("election_data_1.csv")

# Read in the CSV file and create lists
with open(csv1, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	for row in csvreader:
		voter_id.append(row[0])
		county.append(row[1])
		candidate.append(row[2])

# Find the The total number of votes cast

total_votes = (len(voter_id) - 1)

# Complete list of candidates who received votes
n = (int(total_votes))

# Use Counter Module to create a Dictionary with
# Key for candidite names and values for total votes
candidate_list_counter = Counter(candidate)

# Calculate the total number of Candidates and total range of dictionary
t = len(candidate_list_counter)
total_candidates = t - 1

# Create Lists candidate_name and votes from candidate_list_counter
candidate_name = list(candidate_list_counter.keys())
votes = list(candidate_list_counter.values())

# Calcutae percent of votes won for each candiate and store it
for i in range(0, t):
	p = (votes[i] / n) * 100
	percent_won = round(p, 1)
	percent_of_votes.append(percent_won)

# Find the winner
winner = max(candidate_list_counter, key=candidate_list_counter.get)

# Print results
print ("Election Results")
print ("-------------------------")
print ("Total Votes: " + str(total_votes))
print ("-------------------------")
for i in range(1, t):
	print(str(candidate_name[i]) + ": " + str(percent_of_votes[i]) + "% (" + str(votes[i]) + ")")
print ("-------------------------")
print ("Winner: ")
print (winner, candidate_list_counter[winner])
print ("-------------------------")

# Save results as a text file
sys.stdout = open('Election_Results_csv1.txt', 'w')
print ("Election Results")
print ("-------------------------")
print ("Total Votes: " + str(total_votes))
print ("-------------------------")
for i in range(1, t):
	print(str(candidate_name[i]) + ": " + str(percent_of_votes[i]) + "% (" + str(votes[i]) + ")")
print ("-------------------------")
print ("Winner: ")
print (winner, candidate_list_counter[winner])
print ("-------------------------")
sys.stdout.close()