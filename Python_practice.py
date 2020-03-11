counties = ["Arapahoe","Denver","Jefferson"]
counties_tuple = ("Arapahoe","Denver","Jefferson")
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
#if "El Paso" in counties:
    #print("El Paso is in the list of counties.")
#else:
    #print("El Paso is not in the list of counties.")

#if "Arapahoe" in counties and "El Paso" in counties:
    #print("Arapahoe and El Paso are in the list of counties.")
#else:
    #print("Arapahoe or El Paso is not in the list of counties.")

#if "Arapahoe" in counties or "El Paso" in counties:
    #print("Arapahoe or El Paso is in the list of counties.")
#else:
    #print("Arapahoe and El Paso are not in the list of counties.")
    
#for county in counties:
    #print(county)

#for i in range(len(counties)):
    #print(counties[i])

#for county in counties_dict:
    #print(county)

#for county in counties_dict.keys():
    #print(county)

#for voters in counties_dict.values():
    #print(voters)

#for county in counties_dict:
    #print(counties_dict[county])

#for county in counties_dict:
    #print(counties_dict.get(county))

#for county, voters in counties_dict.items():
    #print(county, voters)

#for county, voters in counties_dict.items():
    #print((county)  + " county has "  +  str(voters)  + " registered voters.")

#for county_dict in voting_data:
    #print(county_dict)

#for county_dict in voting_data:
    #for value in county_dict.values():
        #print(value)

#for county_dict in voting_data:
    #print(county_dict['county'])

#my_votes = int(input("How many votes did you get in the election?"))
#total_votes = int(input("What is the total votes in the election?"))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes")

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#for county, voters in counties_dict.items():
    #print(f"{county} county has {voters} registered voters.")

#candidate_votes = int(input("How many votes did the candidate get in the election?"))
#total_votes = int(input("What is the total number of votes in the election?"))
#message_to_candidate = (
    #f"You recieved {candidate_votes} number of votes. "
    #f"The total number of votes in the election was {total_votes}. "
    #f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
#print(message_to_candidate)

#for county, voters in counties_dict.items():
    #print(f"{county} county has {voters:3,} registered voters.")

for i in (voting_data):
    print(f"{i['county']} county has {i['registered_voters']:3,} registered voters.")