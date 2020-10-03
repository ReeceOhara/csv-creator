import csv

#Global const
TIME_INDICATOR = "X"
FIRST_EVENT_MALE_DIVISION = "6-8yrs (male)"
FIRST_EVENT_FEMALE_DIVISION = "6-8yrs (female)"
# SECOND_EVENT_MALE_DIVISION = "6-8yrs (male)"
# SECOND_EVENT_FEMALE_DIVISION = "6-8yrs (female)"
FILE_NAME = "enrolls.csv"

#Reads in specific CSV file and returns three lists corresponding to whichever event an athlete is signed up for
def read_csv():
    #Making the lists
    first_event = []
    second_event = []
    third_event = []
    student_gender = []

    #CSV file layout:
    #id, full name, date time, gender(M/F), date time
    #One or both of the date times wil have an 'X' symbolizing that they are enrolled in that specific date time.

    #Desired CSV layout:
    #first, last, division (age and gender)

    with open(FILE_NAME, 'r') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar='"', skipinitialspace=True)

        for row in filereader:
            time_ind = row.index("X") - 2

            #Add name to correct event list
            if(time_ind == 1):
                first_event.append(row[1].split(sep=", "))
                student_gender.extend([row[1].split(sep=", "), row[2]])
            if(time_ind == 2):
                second_event.append(row[1].split(sep=", "))
                student_gender.extend([row[1].split(sep=", "), row[2]])
            if(time_ind == 3):
                third_event.append(row[1].split(sep=', '))
                student_gender.extend([row[1].split(sep=", "), row[2]])
    
    #Reverse names to get first,last and add divisons
    rev_names(first_event)
    add_div(first_event, student_gender)
    rev_names(second_event)
    add_div(second_event, student_gender)
    rev_names(third_event)
    add_div(third_event, student_gender)

    return first_event, second_event, third_event

#Reverses the elements in ea row of a 2D list
#PARAM: l - Given list to reverse values of
def rev_names(l):
    for row in l:
        row.reverse()

#Adds the 'Division' header to each row in list
#PARAM: l - Given list
#PARAM: s - String object to add to each element
def add_div(l, genderList):
    for row in l:
        gender = get_gender(row[0], genderList)
        # print(gender)
        # print(genderList[1])
        if gender == "Female":
            row.append(FIRST_EVENT_FEMALE_DIVISION)
        else:
            row.append(FIRST_EVENT_MALE_DIVISION)
        

def get_gender(el, genderList):
    for i in genderList:
        if el == i[1]:
            return genderList[genderList.index(i)+1]
        
read_csv()