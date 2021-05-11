# The data we need to retrieve
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# an vailable integer (total vote) to hold the counts of each line registered vote
# need List dictionary to hold candidate names and total number of votes {"CanidateName":CanidateVotes}

# open the data file and read each line data in csv (Ballot ID,County,Candidate)
# Skip 1 read line 

# Loop read line to end file
# increase the total vote by each time read line
# Find canidate name from dictionary
# if found then increase the canidate votes by 1
# else insert the new caidate name and vote = 1
# End Loop

# Loop Dictionary
# find percentage of votes = CanidateVotes / total votes of each candidate in dictionary
# keep the max percentage and canidate name
# End Loop

# print out the winner name with the max percentage

#-------------------------
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter
total_votes = 0
# Candidate Options
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1
        candidate_name = row[2]
        if (candidate_name not in candidate_options):
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #Loop throught items in candidate_votes
    #Caculate percent and print out results
    for candidate in candidate_votes:
        #Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        #Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results,end="")
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # Keep track the max values
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

    # print out the winning candidate, vote count and percentage to terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    #  Save the winner candidate results to our text file.
    txt_file.write(winning_candidate_summary)




