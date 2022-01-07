import csv

codes = list()

with open('codes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    with open('codes.csv', "w"))
    for row in csv_reader:
        for cell in row:
            codes.append(cell.strip())
            print(cell.strip())
    

