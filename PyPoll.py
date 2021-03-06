# The data we need to retrieve:
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote


# Import the datetime dependency.
#import datetime
# Use the now() attribute on the datatime class to get the present time.
#now = datetime.datetime.now()
# Print the present time.
#print("The time right now is, ", now)

# Import csv module.
#import csv
# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
#election_data = open(file_to_load, "r")
#print(election_data)
#Close the file.
#election_data.close()

# Import csv and os modules.
#import csv
#import os
# Add the filname variable that references the path to eleciton_results.csv.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election_results.csv using hte with statement as the filename opject, election_data.
#with open(file_to_load) as election_data:
    #Print the filname object.
    #print(election_data)

#import csv
#import os
# Create a filename variable to direct or indirect path where the file is to be located.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Use the open() function in the "w" mode to open a file and write data to the file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")
# Close the file.
#outfile.close()

#import csv
#import os
# Create a filename variable to direct or indirect path where the file is to be located.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open a file as a text file.
#with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    #txt_file.write("Hello World")

#import csv
#import os
# Create a filename variable to direct or indirect path where the file is to be located.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open a file as a text file.
#with open(file_to_save, "w") as txt_file:
    # Write 3 counties to the file.
    #txt_file.write("Arapahoe")
    #txt_file.write("Denver")
    #txt_file.write("Jefferson")

#import csv
#import os
# Create a filename variable to direct or indirect path where the file is to be located.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open a file as a text file.
#with open(file_to_save, "w") as txt_file:
    # Write 3 counties to the file.
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson, ")

#import csv
#import os
# Create a filename variable to direct or indirect path where the file is to be located.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open a file as a text file.
#with open(file_to_save, "w") as txt_file:
    # Write 3 counties to the file.
    #txt_file.write("Arapahoe, Denver, Jefferson")

#import csv
#import os
# Create a filename variable to direct or indirect path where the file is to be located.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open a file as a text file.
#with open(file_to_save, "w") as txt_file:
    # Write 3 counties on separate lines to the file.
    #txt_file.write("Arapahoe\nDenver\nJefferson")

#import csv
#import os
# Create a filename variable to direct or indirect path where the file is to be located.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open a file as a text file.
#with open(file_to_save, "w") as txt_file:
    # Write 3 counties on separate lines under a header to the file.
    #txt_file.write("Counties in the ELection\n-------------------------\nArapahoe\nDenver\nJefferson")

# Add our dependencies
#import csv
#import os
# Assign a variable to load a file form a path.
#file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
#file_to_save = os.path.join("analysis", "election_analysis.text")
# Open the election results and read the file.
#with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    #file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
    # Print the header row.
    #headers = next(file_reader)
    #print(headers)

# Add our dependencies.
#import csv
#import os
# Assign a variable to load a file form a path.
#file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
#file_to_save = os.path.join("analysis", "election_analysis.text")
# Open the election results and read the file.
#with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    #file_reader = csv.reader(election_data)
    
    # Read the header row.
    #headers = next(file_reader)
    
    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []

# Declare empty dictionary.
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
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

    # Save the results to our text file.
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