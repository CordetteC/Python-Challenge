# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 1 #start from 1 for the january calculation
net_profit_loss = 0 #total profit/loss
total_changes = [] #total change in the profit/loss
greatest_increase = ["",0]
greatest_decrease = ["",float('inf')] 
# float('inf') is used to represent positive infinity in Python. When you initialize a variable with float('inf'), 
#it allows you to set a starting point that is greater than any finite number.


# Open and read the csv
#could also use with open(file_to_load, "r") as financial_data to reduce from 2 lines to 1
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list. Basically saves data for Jan in variable "first row" and THEN skips that row.
    #You do this because you need to store the firs months profit/loss seperately in order for the calculations for net total and change to calculate properly.
    January = next(reader)

    # Track the total and net change
    #formulas below only run once because not inside a loop.
    #This line adds the profit/loss value from the first row (January's data) to the net_profit_loss variable. 
    # The int(first_row[1]) converts the profit/loss value from a string (as read from the CSV) to an integer, allowing you to perform numerical calculations. 
    # After this line executes, net_profit_loss will hold the total profit/loss for the first month.
    net_profit_loss+= int(January[1])
    previous_net = int(January[1]) #setting up previous net to start from January

    # Process each row of data
    for row in reader:

        # Track the totals
        total_months+=1
        net_profit_loss+=int(row[1])
        # Calculate the net change
        net_change = int(row[1]) - previous_net
        total_changes.append(net_change) #this line appends (adds) the calculated net_change to the total_changes list

        # Update previous_net for the next month/iteration
        previous_net = int(row[1])

        # Check for greatest increase
        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]: #checks if current net change is greater than the current recorded greatest increase (which we started at 0)
            greatest_increase[0] = row[0]  # Month
            greatest_increase[1] = net_change  # Amount

        # Check for greatest decrease
        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]: #checks if current net change is less than the current recorded greatest decrease (which we started at 999999)
            greatest_decrease[0] = row[0]  # Month
            greatest_decrease[1] = net_change  # Amount
    
        #^adds the current rows profit/loss to the previous_net amount. I think we're using previous net in 2 different ways. 
        #once to calculate change for the individual months, and once to calculate net change for all months combined so far.
# Calculate the average net change across the months
average_change= sum(total_changes)/len(total_changes) if total_changes else 0
#Using total_changes: This list contains all the calculated monthly changes, so you should sum this list to get the total change over all months.
#Using len(total_changes) gives you the number of changes recorded, which corresponds to the number of months minus the first month (January) since you started tracking changes from the second month onward.
#The if total_changes else 0 part is a safeguard to avoid division by zero in case there are no changes recorded (though in your case, there should always be at least one change).

# Generate the output summary/Print the output
#You’ll use a "formatted string," which is like a template that lets you insert numbers and values (like your calculated profit/loss) right where you want them in a sentence.
#Think of this formatted string as a fill-in-the-blanks sheet where values will automatically show up where they belong.
output_summary = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Profit/Loss: ${net_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"  # Formatting to 2 decimal places
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output summary
print(output_summary)
# Export the results to the specified output file
with open(file_to_output, 'w') as file:
    file.write(output_summary)