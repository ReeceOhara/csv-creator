import csv

#Global const
TIME_INDICATOR = "X"
FIRST_EVENT_DIVISION = "1pm"
SECOND_EVENT_DIVISION = "2pm"
THIRD_EVENT_DIVISION = "3pm"
FILE_NAME = "enrolled.csv"

#Reads in specific CSV file and returns three lists corresponding to whichever event an athlete is signed up for
def read_csv():
    #Making the lists
    first_event = []
    second_event = []
    third_event = []

    #CSV file layout:
    #id, full name, date time, date time
    #One or both of the date times wil have an 'X' symbolizing that they are enrolled in that specific date time.

    #Desired CSV layout:
    #first, last, division (time)

    with open(FILE_NAME, 'r') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar='"', skipinitialspace=True)

        #Skip header
        next(filereader)
        for row in filereader:
            time_ind = row.index("X") - 1

            #Add name to correct event list
            if(time_ind == 1):
                first_event.append(row[1].split(sep=", "))
            if(time_ind == 2):
                second_event.append(row[1].split(sep=", "))
            if(time_ind == 3):
                third_event.append(row[1].split(sep=', '))
    
    #Reverse names to get first,last and add divisons
    rev_names(first_event)
    add_div(first_event, FIRST_EVENT_DIVISION)
    rev_names(second_event)
    add_div(second_event, SECOND_EVENT_DIVISION)
    rev_names(third_event)
    add_div(third_event, THIRD_EVENT_DIVISION)

    return first_event, second_event, third_event

#Reverses the elements in ea row of a 2D list
#PARAM: l - Given list to reverse values of
def rev_names(l):
    for row in l:
        row.reverse()

#Adds the 'Division' header to each row in list
#PARAM: l - Given list
#PARAM: s - String object to add to each element
def add_div(l, s):
    for row in l:
        row.append(s)

read_csv()