# Import necessary modules
import re
import csv
import time

start = time.clock()

# Read the input file which contains companies and respective patent titles
with open('titles.csv') as csvfile:
    reader = csv.reader(csvfile)
    hadoopfile = {rows[1]: rows[0] for rows in reader}

hadoopfile_names = set([str.split(x.lower(), ' ')[0] for x in hadoopfile.values()])

# Read Fortune 500 copmanies list
with open('500.csv', 'r') as f500file:
    reader = csv.reader(f500file)
    f500_names = [rows[0] for rows in reader]

# Write output file accumulating all the companies with their patent titles
output_fullFile = open('titlesVsCompanies14_3', 'w')

j = 0
while j < len(f500_names):
    company_name = f500_names[j]
    desired_value = str.split(f500_names[j].lower(), ' ')
    # Consider two words of the company name if the company name has more than one word
    if len(desired_value) > 1:
        desired_value = desired_value[0]+' '+desired_value[1]
        if desired_value == 'bank of':
            desired_value = desired_value+' '+str.split(f500_names[j].lower(), ' ')[2][0:2]
    else:
        desired_value = desired_value[0]+' '

    # Define data structure for desired output i.e., List of Patent titles for each company
    # by checking company names against Fortune 500 companies
    f500set = [key for key, value in hadoopfile.items() if re.search(r'^%s' % desired_value, value)]

    if f500set:
        # Segregate titles based on company names and store in separate files
        output_file = open(company_name, 'w')

        # Write the titles into the files in required format
        for k in range(0, len(f500set)):
            #output_file.write(f500set[k]+'\n')
            output_fullFile.write(company_name+','+f500set[k]+'\n')
    j = j+1

# Report the complete execution time of the task
print("Execution time:", round((time.clock()-start)/60, 2), "minutes")
