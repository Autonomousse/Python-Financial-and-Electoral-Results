# Import required modules.
import os
import csv

# Create variables and initialize.
# total_months          stores the number of months in the data.
# net_total             stores the sum of all of the profits and losses in the data.
# total                 stores the total value of the monthly changes to calculate the average of the changes in profit/losses.
# value_list            stores the values of profits/losses to be used for calculating the average and finding indices.
# month_list            stores the months to be used to find the corresponding month for greatest increase/decrease in profits.
# average_change_list   stores the values of the changes in profit/losses.

total_months, net_total, total = 0, 0, 0
value_list, month_list, average_change_list = [], [], []

''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
'''  OPEN FILE AND START READING THROUGH ROWS  '''
''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''

# Set the path to collect the data from the Resources folder.
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Read through the CSV.
with open(budget_data_csv, 'r') as csvdatafile:

    # Splits the data at commas.
    csvreader = csv.reader(csvdatafile, delimiter = ',')

    # Skip the header as this is not part of the data.
    header = next(csvreader)

    # Loop through the data by going through every row.
    for row in csvreader:

        # Add 1 for every row to get the number of total months.
        total_months += 1

        # Sum up every row in the Profit/Losses column to get the net total.
        net_total += int(row[1])

        # Create a list with Profit/Losses values.
        value_list.append(int(row[1]))

        # Create a list with the months.
        month_list.append(str(row[0]))

    ''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
    '''  CALCULATE THE AVERAGE OF THE CHANGES IN PROFIT/LOSSES  '''
    ''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''

    # Loop through the list of profit/losses that we stored in value_list.
    for x in range(len(value_list)):
        
        # If the index of the following row (x+1) is less than the number of values stored in the list, then we do the following:
        if x + 1 < len(value_list):

            # Store the value of the next row minus the current row in a variable called change.
            change = value_list[x+1] - value_list[x]

            # Append the value of change into the average_change_list.
            average_change_list.append(change)

    # Store the number of values in average_change_list in length.
    length = len(average_change_list)

    # For every value in the average_change_list, sum the values and store in total:
    for value in average_change_list:

        total += value

    # Calculate the average by dividing the total of the values by the total number of values.
    # Round the average to two decimal places and store it in the average_change variable.
    average_change = round(total/length,2)

    ''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
    '''  FIND GREATEST INCREASE AND GREATEST DECREASE IN PROFITS  '''
    ''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''

    # Use the max() function on average_change_list to find the greatest increase in profits.
    # Find the index where the max value is located.
    # Add 1 to the index to find the month where the greatest increase occurred (average change list is 1 index shorter)
    # Repeat this process to find the greatest decrease in profits using the min() function.
    greatest_inc = max(average_change_list)
    greatest_inc_index = average_change_list.index(greatest_inc)
    greatest_inc_month = month_list[greatest_inc_index + 1]

    greatest_dec = min(average_change_list)
    greatest_dec_index = average_change_list.index(greatest_dec)
    greatest_dec_month = month_list[greatest_dec_index + 1]

    ''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
    '''  PRINT THE RESULTS AND STORE IN A TEXT FILE  '''
    ''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''

    print("Financial Analysis")
    print("--------------------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total:,d}")
    print(f"Average Change: ${average_change:,.2f}")
    print(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc:,d})")
    print(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec:,d})")

    # Specify the file to write to
    output_path = os.path.join("Analysis", "financial_analysis.txt")

    # Open a text file to write to
    analysis_file = open(output_path, 'w')

    # Write the following statements
    analysis_file.write("Financial Analysis \n" +
                        "-------------------------------------------------------- \n" +
                        f"Total Months: {total_months} \n" +
                        f"Total: ${net_total:,d} \n" +
                        f"Average Change: ${average_change:,.2f} \n" +
                        f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc:,d}) \n" +
                        f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec:,d})")

    # Close the text file
    analysis_file.close()