# Program to accumulate the counts for companies

# Import required modules
import re
import csv

# initialize data structures
f500 = []
f500_fullName = []

# Read Fortune 500 company list
with open('500.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        # Splitting the company name based on spaces
        name = str.split(row['F500_Name'], ' ')

        # Assigning parameter criteria - "name"
        # if the company name has more than one word then assign parameter as 1st word and 2nd characters of 2nd word
        # else first word and space
        if len(name) > 1:
            name = name[0]+' '+name[1][0:2]
        else:
            name = name[0]+' '

        # storing all company names in "f500" array
        f500.append(name)

# initialize data structures
completeCount = {}

# Reading Big Data database file
with open('bdwc.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    for rows in reader:
        company_name = re.sub('^[ ]', '', rows['Company_Name'])
        company_name = str.replace(company_name, ' &#x26; ', '&')
        company_name = str.replace(company_name, ',', ' ')
        patent_count = int(rows['Count'])

        # Storing the company names and respective patents count in a dictionary/map
        # If the company name already exists in dictionary/map add the new value to the old key
        # else create a new key-value pair
        if company_name in completeCount.keys():
            completeCount[company_name] = completeCount[company_name] + patent_count
        else:
            completeCount[company_name] = patent_count

out_dict = {}


# Define a procedure
def proc():
    # Create an output file
    output_file = open('11111_first', 'w+')

    # Creating a dictionary/map to store the required key-value pair
    # Check for Fortune 500 company name and store the count
    for x in f500:
        for y in completeCount.keys():
            if re.search(r'^%s' % x, y, re.IGNORECASE):
                if x in out_dict.keys():
                    out_dict[x] = out_dict[x] + completeCount[y]
                else:
                    out_dict[x] = completeCount[y]

                # Creating output file format
                output_file.write(x+','+y+','+str(completeCount[y])+'\n')
    return

# Call the procedure to filter the required Company-Count (key-value) pair
proc()

# Write the Company-Count map into an output file csv
with open('111110_first', 'w+', newline='') as outfile:
    writer = csv.writer(outfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    for key, value in out_dict.items():
        writer.writerow([key, value])
