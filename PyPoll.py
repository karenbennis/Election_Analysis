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


import csv
dir(csv)
file_to_load = 'C:/Users/benni/DataBootcamp/Election_Analysis/Resources/election_results.csv'
reader = csv.reader(file_to_load)
print(reader)
file_variable = open(file_to_load, "r")
