# Import modules
import csv
import os
import sys

# Create a list for each column
date = []
revenue = []

# Open the CSV files
csv1 = os.path.join("budget_data_2.csv")

# Read in the first CSV file
with open(csv1, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	for row in csvreader:
		date.append(row[0])
		revenue.append(row[1])

# Calculate the total number of months included in the dataset

months = (len(date) - 1)

# Calculate the total amount of revenue gained over the entire period

n = (int(months))
sum = 0
for i in range(1,n):
	sum = sum + int(revenue[i])

total_revenue = sum

# Calculate the average change in revenue between months over the entire period
# Use nested if loops to find the greatest increase and greatest decrease
b = 0
greatest_value = 0
least_value = 0
for z in range(1,n):
	a = int(revenue[z]) - int(revenue[z + 1])
	b = b + a
	if a > greatest_value:
		greatest_value = a
		greatest_date = date[z]
	if a < least_value:
		least_value = a
		least_date = date[z]

average_revenue = (b / n)
average_revenue = str(round(average_revenue, 2))

# Print the results
print ("Financial Analysis")
print ("----------------------------")
print ("Total Months: " + str(months))
print ("Total Revenue: " + "$" + str(total_revenue))
print ("Average Revenue Change: " + "$" + str(average_revenue))
print ("Greatest Increase in Revenue:  " + str(greatest_date) + " $" + str(greatest_value))
print ("Greatest Decrease in Revenue:  " + str(least_date) + " $" + str(least_value))

# Save results as a text file
sys.stdout = open('pybank.txt', 'w')
print ("Financial Analysis")
print ("----------------------------")
print ("Total Months: " + str(months))
print ("Total Revenue: " + str(total_revenue))
print ("Average Revenue Change: " + str(average_revenue))
print ("Greatest Increase in Revenue:  " + str(greatest_date) + " " + str(greatest_value))
print ("Greatest Decrease in Revenue:  " + str(least_date) + " " + str(least_value))
sys.stdout.close()
