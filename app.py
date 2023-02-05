from csv import DictReader
from courses import Course


prompt = '\t Have a nice day'
user_input = ''
infos = ['1: Add course', '2: Update an existing course',
         '3: Delete an existing course', '4: Display information about all the courses', '5: Search Course', '6: quit']
course_info = ['course_name', 'course_code',
               'course_prerequizite_code', 'course_credit']
while True:
    for info in infos:
        print(f'{info}\n')
    user_input = int(input(
        'Select your input from these flowing options by pressing the SERIAL NUMBER \n6 EX (1,2,3,4,5,6) FROM 1 TO 6 AND ENTER\n'))

    if user_input == 1:
        '''ADD A Course'''
        courses = []
        for course in course_info:
            courses.append(input(f' \t Type {course} :'))
# if not empty check course exist or not
        if courses[0:4] != '':
            if Course.check(courses[0], courses[1]) == True:
                print('\t this course already exist \n ')
            elif Course.check2(courses[0], courses[1], courses[2]) == False:
                # if course and pre req dosent exist then pass the value to constructor
                course = Course(courses[0], courses[1],
                                courses[2], int(courses[3]))
                course.add_course()
# name ,code ,credit is mendatory
        elif courses[0:2] == '' and courses[3] == '':
            print('course name , code, credit is mendatory \n')
            while True:
                courses[0] = input('\t type course Name ? \n')
                courses[1] = input('\t type course Code ? \n')
                courses[3] = input('\t type course Credit ? \n')
                if courses[0:2] != '' and courses[3] != '':
                    # if name ,code ,credit is not empty then check course exist or not then pre

                    if Course.check(courses[0], courses[1]) == True:
                        print('\t this course already exist \n')
                        break
                    # course dosent exist and pre req dosent exist
                    elif Course.check(courses[0], courses[1]) == False and courses[2] == '':
                        answer = input(
                            '\t would you like to enter a pre_requisite (y/n)\n')
                        if answer == 'y':
                            course[2] = input('\t enter pre requisite')
                            course = Course(
                                courses[0], courses[1], courses[2], int(courses[3]))
                            course.add_course()
                            break
                        else:
                            course = Course(
                                courses[0], courses[1], courses[2], int(courses[3]))
                            course.add_course()
                            break

        '''
        course = Course(courses[0], courses[1], courses[2], int(courses[3]))
        course.add_course()
        '''

# ---------------------------------------------------------------------------------------------------
    elif user_input == 2:
        '''2: Update an existing course'''

        courses = []
        for course in course_info:
            courses.append(input(f'Type {course} :'))

        course = Course(courses[0], courses[1], courses[2], int(courses[3]))

        preamiters = ['updated_code', 'updated_name',
                      'updated_credit', 'updated_pre_requizite']
        details = []
        for peramiter in preamiters:
            details.append(input(f'\tnew {peramiter} :'))
        course.update_course(details[0], details[1],
                             int(details[2]), details[3])

# -------------------------------------------------------------------------------------------------
    elif user_input == 3:
        '''3: Delete an existing course'''
        courses = []
        courses.append(input('Course Name: \t'))
        courses.append(input('Course code: \t'))
        courses.append(input('Course pre_requisite: \t'))
        courses.append(int(input('Course cratid: \t')))

        course = Course(courses[0], courses[1], courses[2], courses[3])
        course.delate_course(courses[1])

    elif user_input == 4:
        Course.display_course('add')

    elif user_input == 5:
        '''Search Course
        '''
        course_name = input('Enter course name : ')
        course_Code = input('Enter course code : ')

        Course.search_course(course_name, course_Code)

    elif user_input == 6:
        break
    else:
        print('please enter valid input')

print(prompt)
