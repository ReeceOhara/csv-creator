def getUserNames():
    first_name = ''
    last_name = ''

    fNames = []
    lNames = []

    question_ans = input('Do you have values? Y/n')

    while question_ans == 'Y':
        first_name = input('Enter first name: ')
        fNames.append(first_name)

        last_name = input('Enter last name: ')
        lNames.append(last_name)

        question_ans = input('Do you have more values? Y/n')

    return fNames, lNames