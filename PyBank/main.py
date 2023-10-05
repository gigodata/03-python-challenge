# main.py

# Script for PyBank analysis using Python - Module 03 - MSU Data Analytics Bootcamp
# Result returned is a summary analysis of MOM changes in P&L over 7+ yearly period.
# Created: 2023-09-27
# Last Modified: 2023-10-05
# Author: Adrian Santos
# v1.0

# Notes: 	Worked with fellow student, Michael Moore. His approach is very different from mine, and mine is what makes sense to me.
#			Had tutoring assistance from Reza Abasaltian to get past the roadblocks in the approach that I have taken in this analysis.
#			I used Bing to ask for help on how to export the results to a text file.
###############################################################

# Import Python module to create file paths across operating systems
import os

# Clear screen so output is clean & fresh for output of results
os.system('clear')

# Import Python module used to read CSV files
import csv

# Define file_name
# The 
file_name = "/Users/adrian/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"

month = [] # First column of data in CSV file is Month in 'Mmm-YY' format
MOM_delta = [] # container for month-on-month changes in P&L
current_pnl = 0
cuml_pnl = 0

# Open the CSV file as read in data
with open(file_name) as csvfile:

    # CSV reader specifies delimiter and variable used as container for data in CSV file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the first row as the header names for this dataset
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        delta = int(row[1]) - current_pnl 
        MOM_delta.append(delta)     
        current_pnl = int(row[1])
        cuml_pnl = cuml_pnl + current_pnl
        month.append(row[0])
        
MOM_delta.pop(0) # deletes first item from the list
month.pop(0) # deletes equivalent row from list

average_pnl = sum(MOM_delta) / len(MOM_delta)					# Calculates the average of MOM_delta in P&L
index_month_max = MOM_delta.index(max(MOM_delta))				# This captures the index associated with the month that has the hight MOM_delta
index_month_min = MOM_delta.index(min(MOM_delta))				# This captures the index associated with the month that has the lowest MOM_delta


formatted_average_pnl = "(${:,.2f})".format(float(average_pnl))		# This formats the average P&L to only two decimals--need more understanding on formatting
formatted_total_pnl = "${:,.0f}".format(cuml_pnl)				# This formats the total P&L to currency, with commas, 0 decimals -- for readability
formatted_max_MOM_delta = "${:,.0f}".format(max(MOM_delta))				# This formats the total P&L to currency, with commas, 0 decimals -- for readability
formatted_min_MOM_delta = "(${:,.0f})".format(min(MOM_delta))				# This formats the total P&L to currency, with commas, 0 decimals -- for readability

############################
# Begin Output to Terminal #
############################

print()				# Insert a beginning blank line for readability
print("Financial Analysis")
print("----------------------------")
print("Total Months: ", len(MOM_delta) + 1) # Outputs the total number of row -- adds +1 back, due to pop-off (removal) of original row_01 of data array--no MOM_delta possible
print("Total P&L: ",formatted_total_pnl)		# Returns formatted total P&L
print("Average Month-on-Month Change: ",formatted_average_pnl)		# Returns average P&L
print("Greatest Increase in Profits: ", month[index_month_max], "\t", formatted_max_MOM_delta)			# First part returns the associated month - Second part returns the formatted max MOM_detail
print("Greatest Decrease in Losses: ", month[index_month_min], "\t", formatted_min_MOM_delta)			# First part returns the associated month - Second part returns the formatted min MOM_detail
print()				# Insert a final blank line for readability

# NOTE: Only negative numbers have parentheses around them; positive numbers never have parentheses around them--it would misconstrue the value as negative.
# The script provides clearer labels and proper number/currency formatting. A 'negative profit' is not a profit; it is called a loss.


#############################
# Begin Output to Text File #
#############################

with open('budget_data_output.txt', 'w') as f:
    f.write('Financial Analysis\n')
    f.write('----------------------------\n')
    f.write('Total Months: ' + str(len(MOM_delta) + 1) + '\n')
    f.write('Total P&L: ' + str(formatted_total_pnl) + '\n')
    f.write('Average Month-on-Month Change: ' + str(formatted_average_pnl) + '\n')
    f.write('Greatest Increase in Profits: ' + str(month[index_month_max]) + '\t' + str(formatted_max_MOM_delta) + '\n')
    f.write('Greatest Decrease in Losses: ' + str(month[index_month_min]) + '\t' + str(formatted_min_MOM_delta))
	
# End of Script