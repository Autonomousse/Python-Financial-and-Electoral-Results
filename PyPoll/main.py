# Import required modules.
import os
import csv

# Create variables and initialize.
# total_votes       will count and hold the total number of votes.
# candidates        will be a list of candidate names that will be used to make all the calculations.
# votes             will store the number of votes each unique candidate received.
# sort_votes        will be used to sort the number of votes in descending order.
# sort_candidates   will be used to sort the candidates in the same order as the votes they received in vote_sort.
# percentages       will hold the percentage of votes each candidate has.

total_votes = 0
candidates, votes = [], []
sort_votes, sort_candidates = [], []
percentages = []

''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
'''  OPEN FILE AND START READING THROUGH ROWS  '''
''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''

# Set the path to collect the data from the Resources folder.
election_data_csv = os.path.join("Resources", "election_data.csv")

# Read through the CSV.
with open(election_data_csv, 'r') as csvdatafile:

    # Splits the data at commas.
    csvreader = csv.reader(csvdatafile, delimiter = ',')

    # Skip the header as this is not part of the data.
    header = next(csvreader)

    # Loop through the data by going through every row.
    for row in csvreader:
        
        # Add 1 for every row to count the number of votes.
        total_votes += 1

        # Create a list of the candidates that were voted for.
        candidates.append(str(row[2]))

    # Use the set() function to find all unique candidate names.
    unique_candidates = set(candidates)

    # Convert the set to a list.
    candidate_list = list(unique_candidates)

    # Create a list with zeros as placeholders for the number of unique candidates.
    for unique in range(len(candidate_list)):
        votes.append(0)

    ''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
    '''  TALLY UP VOTES PER CANDIDATE  '''
    ''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''

    # Iterate through the names in the candidates list.
    for name in range(len(candidates)):

        # Iterate through the candidate_list which has the unique candidate names.
        for x in range(len(candidate_list)):

            # If the name in the entire candidate list matches a name in the unique candidate_list,
            # add 1 to the unique candidates vote count in the same index in the vote list.
            if candidates[name] == candidate_list[x]:

                votes[x] += 1

    ''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
    '''  CREATE DESCENDING LISTS OF CANDIDATES AND THE NUMBER OF VOTES THEY RECEIVED  '''
    ''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''

    # Loop through the length of the votes list until no values are left in the list.
    for x in range(len(votes)):

        # If there are no values left in the list, then break the loop.
        if len(votes) == 0:
            break

        # If there are values in the list, find the max number of votes in the votes list.
        # Append the max_votes value to a new sort_votes list. This will store the votes in descending order.
        # Find the index where the max_votes value was stored in the votes list.
        # Pass the max_index to the candidates_list to find the candidate who received the max votes and append the name to the same index in the sort_candidates list.
        # (This allows us to have a descending list of candidates and the number of votes they received)
        # Remove the max number of votes from the votes list and the name of the candidate who received them from the candidate list.
        max_votes = max(votes)
        sort_votes.append(max_votes)
        max_index = votes.index(max_votes)
        sort_candidates.append(candidate_list[max_index])
        votes.pop(max_index)
        candidate_list.pop(max_index)

    ''' ~~~~~~~~~~~~~~~~~~~~~~~ '''
    '''  CALCULATE PERCENTAGES  '''
    ''' ~~~~~~~~~~~~~~~~~~~~~~~ '''

    # For every value in the sort_votes list, calculate the percent of total votes and store the values in a new list called percentages.
    for value in range(len(sort_votes)):

        calculate = (sort_votes[value] / total_votes)
        percentages.append(calculate)

    ''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
    '''  PRINT THE RESULTS AND STORE IN A TEXT FILE  '''
    ''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''

    print("Election Results \n" +
          "---------------------------- \n" +
          f"Total Votes: {total_votes:,d} \n" +
          "---------------------------- \n")

    for results in range(len(sort_votes)):

        print(f"{sort_candidates[results]}: {percentages[results]:.3%} ({sort_votes[results]:,d}) \n")

    print("---------------------------- \n" +
          f"Winner: {sort_candidates[0]} \n" +
          "----------------------------")

    # Specify the file to write to
    output_path = os.path.join("Analysis", "election_results.txt")

    # Open a text file to write to
    election_file = open(output_path, 'w')

    # Write the following statements
    election_file.write("Election Results \n" +
                        "---------------------------- \n" +
                        f"Total Votes: {total_votes:,d} \n" +
                        "---------------------------- \n")

    for results in range(len(sort_votes)):

        election_file.write(f"{sort_candidates[results]}: {percentages[results]:.3%} ({sort_votes[results]:,d}) \n")

    election_file.write("---------------------------- \n" +
                        f"Winner: {sort_candidates[0]} \n" +
                        "----------------------------")
