import csv
import get_names
import read_csv

#CONSTANTS
FIRST_FILE_NAME = "mini_first_event.csv"
SECOND_FILE_NAME = "mini_second_event.csv"
THIRD_FILE_NAME = "mini_third_event.csv"

#GETTING THE ENROLLMENTS FOR EACH EVENT
FIRST_EVENT, SECOND_EVENT, THIRD_EVENT = read_csv.read_csv()

#These three are responsible for writing to three different files. The process is roughly the same. The names of ea file are different
def write_first():
    with open(FIRST_FILE_NAME, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

        write_data(FIRST_EVENT, filewriter)

def write_second():
    with open(SECOND_FILE_NAME, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

        write_data(SECOND_EVENT, filewriter)

def write_third():
    with open(THIRD_FILE_NAME, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

        write_data(THIRD_EVENT, filewriter)

#Return the number of columns in a list
#PARAM: l - Given list
#RETURN: Number of COLUMNS in list
def get_num_cols(l):
    if(len(l) == 0):
        return 0

    return len(l[0])

#Writes data to a file given a filewriter object
#PARAM: event - The list of names for that specific event
#PARAM: fw - The csv.writer object
#Return: writes rows to filewriter object to write to file
def write_data(event, fw):

    if(get_num_cols(event) == 2):
        fw.writerow(['First Name', 'Last Name'])
        for row in event:
            fw.writerow(row)

    if(get_num_cols(event) == 3):
        fw.writerow(['First Name', 'Last Name', 'Division'])
        for row in event:
            fw.writerow(row)

#Runs the program
def runner():

    if len(FIRST_EVENT) > 0:
        write_first()
    
    if len(SECOND_EVENT) > 0:
        write_second()
    
    if len(THIRD_EVENT) > 0:
        write_third()

    print("Successfully wrote all athletes to files")

    return
runner()