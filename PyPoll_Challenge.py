#(1) The data we need to retrieve
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# A complete list of counties where votes casted
# Total number of votes each county casted

#(2) The calculated data to save to file and to terminal
# total number of votes
# Percentage of votes each county casted
# The largest county votes casted
# Percentage of votes each candidate won
# The winner of the election based on popular vote
#-------------------------
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# County Name and Votes Dictionary 
# Initilize the empty dictionary 
county_votes = {}

# 2: Track the largest county and county voter turnout.
largest_county_vote = ""
largest_votes = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    headers = next(reader)

     # For each row in the CSV file.
    for row in reader:
        #Add to the total vote count
        total_votes = total_votes+1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.

        # If the candidate does not match any existing candidate add it to
        # the candidate list

        if (candidate_name not in candidate_votes.keys()):

             # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
       # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        
        county_name = row[1]
        if (county_name not in county_votes.keys()):
            county_votes[county_name] = 0

         # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    
    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
  
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county in county_votes:

       # 6b: Retrieve the county vote count.
        county_vote_count = county_votes[county] 

       # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage = (county_vote_count/total_votes)*100

       # 6d: Print the county results to the terminal.
        county_results = (f"{county}: {county_vote_percentage:.1f}% ({county_vote_count:,})\n")
        print(county_results,end="")

        # 6e: Save the county votes to a text file.

        txt_file.write(county_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if county_vote_count > largest_votes :
            largest_votes = county_vote_count
            largest_county_vote = county

  # 7: Print the county with the largest turnout to the terminal.
    largest_vote_county_results = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county_vote}\n"
        f"-------------------------\n")
    print(largest_vote_county_results,end="")

  # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_vote_county_results)

   
  # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage

        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    #  # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------")
    print(winning_candidate_summary)
    
    #  Save the winner candidate results to our text file.
    txt_file.write(winning_candidate_summary)




