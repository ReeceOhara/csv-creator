import csv

def read_csv():
    #Making the lists
    two_enr = []
    three_enr = []

    #CSV file layout:
    #id, full name, date time, date time
    #One or both of the date times wil have an 'X' symbolizing that they are enrolled in that specific date time.

    #Desired CSV layout:
    #first, last, division (time)

    with open('enrolled.csv', 'r') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar='"', skipinitialspace=True)

        next(filereader)
        for row in filereader:
            # names.append(row[1].split())
            time_ind = row.index("X") - 2

            if(time_ind == 1):
                two_enr.append(row[1].split(sep=", "))
            else:
                three_enr.append(row[1].split(sep=", "))
    
    rev_names(two_enr)
    add_div(two_enr, "2pm")
    rev_names(three_enr)
    add_div(three_enr, "3pm")

    #Testing
    # print("2pm:")
    # for i in two_enr:
    #     print(i)

    # print("3pm:")
    # for k in three_enr:
    #     print(k)

    return two_enr, three_enr

def rev_names(l):
    for row in l:
        row.reverse()

def add_div(l, s):
    for row in l:
        row.append(s)