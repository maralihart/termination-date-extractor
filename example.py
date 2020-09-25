import csv
import re

"""
This code takes in data and searches in the appropriate cell to find termination shortkeys and then extracts the dates. 
"""

# https://stackoverflow.com/questions/11070527/how-to-add-a-new-column-to-a-csv-file under Creative Commons License
 
filename = input("What is the file name? Please put file extension.  ")
outputName = input("What would you like to output it to? Please put file extension.  ")
column = int(input("What column is the data in? (A = 1, B = 2, etc.)  ")) + 1
 
with open(filename,'r') as csvinput, open(outputName, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)
 
        output = []
        header = next(reader)
        header.append('Termination Date')
        output.append(header)
 
        for row in reader:
            print(row[0],row[column])
            if "TERM" in row[column] or "TRMD" in row[column]:
                date = re.search("([0-9]+[\/|\.|-])([0-9]+)([\/|\.|-]([0-9]{4}|[0-9]{2})|)?", row[column])
                try:
                    date = date.group(0)
                    row.append(date)
                except:
                    row.append("No Date Given")
            output.append(row)
 
        writer.writerows(output)