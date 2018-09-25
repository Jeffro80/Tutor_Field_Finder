# Tutor Field Finder
# Version 0.1 25 September 2018
# Created by Jeff Mitchell
# Returns a list of students who have the provided Tutor name in their
# Custom Field
# Data is sourced from the 'Student Course Information' report from the
# Learning Platform Ad-hoc database query

# To Do:

# Add a count of the number of students returned and display

import csv
import time


def debug_list(test_list):
    """Print out contents of a list.
   
    Args:
        test_list (list): List to be printed out.
    """
    i = 0
    while i < len(test_list):
        print('Item ' + str(i))
        print(str(test_list[i]))
        i += 1


def get_load_file_name():
    """Get the name of the file to be loaded.
    
    Returns:
        file_name (str): Name of file to be loaded.
    """
    file_name = ''
    valid_file = False
    while valid_file is not True:
        file_name = input('What file would you like to load with the '
                          'student data? ')
        try:
            f = open(file_name + '.csv', 'r')
        except IOError:
            print('\nSorry, that file does not exist. Please try again.')
        else:
            valid_file = True
    return file_name


def generate_time_string():
    """Generate a timestamp for file names.

    Returns:
        time_str (str): String of timestamp in the format yymmdd-hhmmss.
    """
    time_str = time.strftime('%y%m%d-%H%M%S')
    return time_str


def load_csv_data(file_name):
    """Load a csv file.
    
    Args:
        file_name (str): Name of file to be loaded.
        
    Returns:
        csv_data (list): Data that has been loaded.
    """
    csv_data = []
    # Check that file exists
    valid_file = False
    while valid_file is False:
        try:
            file = open(file_name + '.csv', 'r')
        except IOError:
            print('The file does not exist. Check file name.')
            file_name = input('What is the name of the file? ')
        else:
            file.readline()
            reader = csv.reader(file, delimiter=',', quotechar='"')
            for row in reader:
                if row[0] not in (None, ''):
                    csv_data.append(row)
            file.close()
            print('\nData has been loaded.')
            valid_file = True
    return csv_data


def main():
    main_message()
    f_name = get_load_file_name()
    tutor = input('\nWhat is the full name of the tutor to look for? ')
    s_name = 'Students_' + generate_time_string()
    student_data = load_csv_data(f_name)
    # debug_list(student_data)
    found_students = process_students(student_data, tutor)
    headings = ['Student ID', 'First Name', 'Last Name']
    save_students(found_students, headings, s_name)


def main_message():
    """Print the main message."""
    print('\n\n*************==========================*****************')
    print('\nTutor Field Finder version 0.1')
    print('Created by Jeff Mitchell, 2018')


def process_students(student_data, tutor):
    """Find students with the identified tutor.
    
    Looks for the string for the desired Tutor within the data field for each
    student. If the tutor is found the Student ID, First Name and Last Name of
    the student are added to the list that is returned.
    
    Args:
        student_data (list): Student data to be checked.
        tutor (str): The tutor to look for.
        
    Returns:
        missing_students (list): Students that are missing their Student ID.
    """
    found_students = []
    for student in student_data:
        this_student = []
        if tutor in student[3]:
            this_student.append(student[0])
            this_student.append(student[1])
            this_student.append(student[2])
            found_students.append(this_student)
    return found_students


def save_students(input_data, headings_data, file_name):
    """Save the data to a CSV file.
    
    Args:
        input_data (list): Data to be saved.
        headings_data (list): Column headings to be used.
        file_name (str): File name to be saved to.
    """
    i_data = input_data
    headings = headings_data
    d_name = file_name
    f_name = file_name + '.csv'
    try:
        open(f_name, 'w')
    except IOError:
        print('Unable to save ' + d_name + ' Data. Please try again.')
    else:
        with open(f_name, 'w', newline='') as csv_file:
            headingWriter = csv.DictWriter(csv_file,
                                           fieldnames=headings)
            headingWriter.writeheader()
            writer = csv.writer(csv_file)
            for item in i_data:
                writer.writerows([item])
        print(d_name + ' has been saved to ' + f_name)
    return


if __name__ == '__main__':
    main()