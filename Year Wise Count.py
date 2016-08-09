# Program to find companies which have zero patent count

# Import required modules
import csv
import re

with open('patentcount/2006_orgname.txt', 'r') as company_names:
    company_list = company_names.readlines()

y = {}
for x in company_list:
    x = re.sub('^[ ]+', '', x)
    x = re.sub('[ ]', ',', x, count=1)
    print(x)
    x = str.split(x, ',')
    y[x[1]] = x[0]

print(len(y))

quit()
# Read Fortune 500 company list
with open('500.csv') as f500file:
    reader = csv.reader(f500file)
    f500 = [rows[0] for rows in reader]

# Read Fortune 500 Company names which have at least one patent
pat_comp = {}
fName = str(2005)
filename = 'patentcount/'+fName+'.csv'
with open(filename) as patentcompanies:
    reader = csv.reader(patentcompanies)
    pat_comp = {rows[1]:int(rows[0]) for rows in reader}

# Condition to check missing company names
# Print the missing companies on command prompt
map = {}
for x in f500:
    for y in pat_comp.keys():
        if re.search(r'^%s' %x, y, re.IGNORECASE):
            if x in map.keys():
                map[x] = map[x]+ pat_comp[y]
            else:
                map[x] = pat_comp[y]

filename = 'patentcount/f500_'+fName+'.csv'
with open(filename, 'w', newline='') as outfile:
    writer = csv.writer(outfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['company name','count','year'])
    for key in map.keys():
        writer.writerow([key, map[key],fName])