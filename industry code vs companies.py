# Program to assign Industry sectors to the Fortune 500 companies

# Import required modules
import csv

# Read industry code vs name reference file
with open('indcodes.csv') as indcodes:
    reader = csv.reader(indcodes)
    indmap = {rows[0]: rows[1] for rows in reader}

# Declare data structure
groupcount = {}

# Read Code vs Fortune 500 Name file
with open('code_name_count.csv') as cncfile:
    reader = csv.DictReader(cncfile)
    # Write the respective Industry sector to the Fortune 500 company
    with open('code_ouput.csv', 'w+', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Code', 'Name', 'Count', 'Industry'])
        for rows in reader:
            code = rows['Code']
            name = rows['Name']
            count = int(rows['Count'])
            parent_code = code[0:2]
            writer.writerow([code, name, count, indmap[parent_code]])
            # Accumulate the patent counts grouped by parent Industry code into a python map
            if parent_code in groupcount.keys():
                groupcount[parent_code] = groupcount[parent_code] + count
            else:
                groupcount[parent_code] = count

# Write the Industry name vs Accumulated Count
with open('industry_count.csv', 'w+', newline='') as outfile:
    writer = csv.writer(outfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)

    # Define header in the output file
    writer.writerow(['Industry', 'Count'])
    for key, value in groupcount.items():
        writer.writerow([indmap[key], value])
