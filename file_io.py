# Part I
import csv

student_list = []
with open('students.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    rows = list(reader)
    for row in rows:
        student_list.extend(row)

# print(student_list)


def add_student(first_name):
    with open("students.txt", "a+") as file:
        file.write("{}\n".format(first_name))
    print("{} added to students.".format(first_name))


def find_student(first_name):
    try:
        print("{} first found at index {}.".format(
            first_name, student_list.index(first_name)))
    except ValueError as err:
        print(err)


# bonus
def update_student(first_name, new_name):
    try:
        print("{} first found at index {}.".format(
            first_name, student_list.index(first_name)))
        student_list[student_list.index(first_name)] = new_name
        with open("students.txt", "w") as file:
            for name in student_list:
                file.write("{}\n".format(name))
        print("{} is now {} at index {}.".format(
            first_name, new_name, student_list.index(new_name)))
    except ValueError as err:
        print(err)


def remove_student(first_name):
    try:
        print("{} first found at index {}.".format(
            first_name, student_list.index(first_name)))
        student_list.remove(first_name)
        with open("students.txt", "w") as file:
            for name in student_list:
                file.write("{}\n".format(name))
        print("{} is now removed from previous index.".format(first_name))
    except ValueError as err:
        print(err)


# add_student("lydia") # added to end
# find_student("bob") # index 0
# find_student("amy")  # case where doesn't exist


# bonus 1 - write additional functions
# update_student("bob", "sam") # index 0 changed
# update_student("amy", "alicia") # case where doesn't exist
# remove_student("bob")
# remove_student("amy")  # case where doesn't exist

# bonus 2 - unique id for each student
# need to think about more...

# Part II
def print_names(): # names are already in first,last order
    with open('users.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rows = list(reader)
        for row in rows:
            print(' '.join(row))

def enter_names(first, last):
    with open('users.csv', 'a') as csvfile:
        data_writer = csv.writer(csvfile, delimiter=",")
        data_writer.writerow([first,last])

# print_names()
# enter_names("Ragnarr","Neoptolemus")