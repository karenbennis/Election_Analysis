# Add dependencies.
import csv
import os
# Assign a variable to load election results file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the text file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Declare empty list for 'county options'
county_options = []

# Declare empty dictionary for 'county votes'.
county_votes = {}

# Initialize variables for 'largest county turnout' and 'largest count'
largest_turnout = ""
largest_count = 0

# Declare empty list for 'candidate options'
candidate_options = []

# Declare empty dictionary for 'candidate votes'.
candidate_votes = {}

# Initialize variables for 'winning candidate' and 'winning count' and 'winning percentage'
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the csv file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes += 1

        # Print the county name from each row.
        county_name = row[1]

        # If the county does not match any existing county...
        if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)

            # Begin tracking that county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that county's count.
        county_votes[county_name] += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Save the results to the text file.
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
        
        # Print 'County Votes' as a heading to the terminal.
        county_heading = (f"\nCounty Votes:\n")
        print(county_heading)
        # Save the 'County Votes' heading to the text file.
        txt_file.write(county_heading)

        for county in county_votes:
            # Retrieve vote count from a county.
            votes = county_votes[county]
            # Calculate the percentage of votes from a county.
            vote_percentage = float(votes) / float(total_votes) * 100
            county_results = (
                f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        
            # Print each county, its voter count and percentage to the terminal.            
            print(county_results)
            # Save the county results to the text file.
            txt_file.write(county_results)

            # Determine largest county turnout.      
            if (votes > largest_count):
                largest_count = votes
                largest_turnout = county

    # Print out the largest turnout to terminal.    
        largest_turnout_summary = (
            f"\n-------------------------\n"
            f"Largest County Turnout: {largest_turnout}\n"
            f"-------------------------\n")
        print(largest_turnout_summary)
        # Save the largest turnout to the text file.
        txt_file.write(largest_turnout_summary)

        for candidate in candidate_votes:
            # Retrieve vote count of a candidate.
            votes = candidate_votes[candidate]
            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        
            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            # Save the candidate results to our text file.
            txt_file.write(candidate_results)

            # Determine winning vote count, winning percentage, and winning candidate      
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate

    # Print out the winning candidate, vote count and percentage to terminal.    
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        # Save the candidate results to our text file.
        txt_file.write(winning_candidate_summary)