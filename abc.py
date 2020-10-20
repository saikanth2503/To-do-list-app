import csv 

with open('test.txt') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    linecount = 0
    for row in csvReader:
        if linecount == 0:
            print(f"Column names are {','.join(row)}")