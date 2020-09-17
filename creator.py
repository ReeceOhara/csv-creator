import csv
import get_names
import read_csv

# fNames = []
# lNames = []
# divisions = []

# fNames, lNames = get_names.getUserNames()

FIRST_EVENT, SECOND_EVENT = read_csv.read_csv()

def write_csv():
    with open('competitors.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

        if(get_num_rows(FIRST_EVENT) == 2):
            filewriter.writerow(['First Name', 'Last Name'])
            for row in FIRST_EVENT:
                filewriter.writerow(row)
                print(row)
        elif(get_num_rows(FIRST_EVENT) == 3):
            filewriter.writerow(['First Name', 'Last Name', 'Division'])
            for row in FIRST_EVENT:
                filewriter.writerow(row)
                print(row)

        ##Loop through both arrays and add their eq values to rows in csv
        # for i, k in zip(fNames, lNames):
        #     filewriter.writerow([i, k])
        #     print('' + i + ',' + k)

def get_num_rows(l):
    return len(l[0])

write_csv()