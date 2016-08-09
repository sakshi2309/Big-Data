# Program to find companies which have zero patent count

# Import required modules
import csv

# Read Fortune 500 company list
with open('500.csv') as f500file:
    reader = csv.reader(f500file)
    f500 = [rows[0] for rows in reader]

# Read Fortune 500 Company names which have at least one patent
with open('777771_first.csv') as foundcompanies:
    reader = csv.reader(foundcompanies)
    found_comp = [rows[0] for rows in reader]

# Condition to check missing company names
# Print the missing companies on command prompt
for x in f500:
    if x not in found_comp:
        print(x)