import csv
import get_names

fNames = []
lNames = []

fNames, lNames = get_names.getUserNames()

with open('competitors.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    filewriter.writerow(['First Name', 'Last Name'])

    ##Loop through both arrays and add their eq values to rows in csv
    for i, k in zip(fNames, lNames):
        filewriter.writerow([i, k])
        print('' + i + ',' + k)
