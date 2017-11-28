# Import modules
import csv
import os

# Create a list for each column
date = []
revenue = []

# Open the CSV files
csv1 = os.path.join("budget_data_1.csv")

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
c = 0
for z in range(1,n):
	a = int(revenue[z]) - int(revenue[z + 1])
	b = a / int(revenue[z])
	c = c + b

average_revenue = (c / n) * 100

# Find the greatest decrease in revenue (date and amount) over the entire period
for x in range(1,n):	
	if int(revenue[x]) < int(revenue[x + 1]):
		least_value = int(revenue[x])
		least_date = str(date[x])
		continue

# Find the greatest increase in revenue (date and amount) over the entire period
for y in range(1,n):
	if int(revenue[y]) > int(revenue[y + 1]):
		greatest_value = int(revenue[i])
		greatest_date = str(date[i])
		continue

# Print the results

print ("Financial Analysis")
print ("----------------------------")
print ("Total Months: " + str(months))
print ("Total Revenue: " + str(total_revenue))
print ("Average Revenue Change: " + str(average_revenue) + "%")
print ("Greatest Increase in Revenue:  " + str(greatest_date) + " " + str(greatest_value))
print ("Greatest Decrease in Revenue:  " + str(least_date) + " " + str(least_value))

# Save results as a text file
