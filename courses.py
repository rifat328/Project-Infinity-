from csv import writer
from csv import DictWriter, DictReader
import pandas as pd
from tempfile import NamedTemporaryFile
import shutil


class Course:
    def __init__(self, course_name: str, course_code: str, course_prerequizite_code: str, course_credit: int):
        assert course_credit >= 0, 'credit cant be negative number'

        self.course_name = course_name
        self.course_code = course_code
        self.course_prerequizite_code = course_prerequizite_code
        self.course_credit = course_credit

    def add_course(self):
        '''with open('course_data_updated.csv', 'w') as file:'''

        with open('course_data_updated.csv', 'a') as file:
            header = ('Index', 'Code', 'Name', 'Credit', 'Pre-Requisite')
            index = 'Index'
            key_course_code = 'Code'
            key_course_name = 'Name'
            key_course_credit = 'Credit'
            key_course_prerequizite_code = 'Pre-Requisite'
            csv_writer = DictWriter(
                file, fieldnames=header, lineterminator='\n')
            df = pd.read_csv('course_data_updated.csv')
            count = df['Index'].max()
            count += 1
            # csv_writer.writeheader()
            csv_writer.writerow(
                {
                    index: count,
                    key_course_code: self.course_code,
                    key_course_name: self.course_name,
                    key_course_credit: self.course_credit,
                    key_course_prerequizite_code: self.course_prerequizite_code


                }
            )

    def delate_course(self, del_course):
        with open('course_data_updated.csv', 'r+') as file:
            csv_reader = DictReader(file)
            data = list(csv_reader)

        flag = 0

        with NamedTemporaryFile(mode='w', delete=False) as temp_file:
            header = ('Index', 'Code', 'Name', 'Credit', 'Pre-Requisite')
            csv_writer = DictWriter(
                temp_file, fieldnames=header, lineterminator='\n')
            csv_writer.writeheader()
            for row in data:
                if row['Code'] == del_course:
                    flag = 1
                    continue
                csv_writer.writerow(row)

        if flag == 1:
            temp_path = temp_file.name  # jamela indentation
            shutil.move(temp_file.name, 'course_data_updated.csv')
            print('your course got successfully deleted ')
        elif flag == 0:
            print('your course dosent exist ')

    def display_course(self):
        with open('course_data_updated.csv', 'r') as file:

            csv_reader = DictReader(file, lineterminator='\n')
            for row in csv_reader:
                print(row)

    def update_course(self, updated_code, updated_name, updated_credit, updated_pre_requizite):
        with open('course_data_updated.csv', 'r') as file:
            csv_reader = DictReader(file)
            data = list(csv_reader)

        with NamedTemporaryFile(mode='w', delete=False) as temp_file:
            header = ('Index', 'Code', 'Name', 'Credit', 'Pre-Requisite')

            csv_writer = DictWriter(
                temp_file, fieldnames=header, lineterminator='\n')
            csv_writer.writeheader()

            for row in data:
                if row['Name'] == self.course_name or row['Code'] == self.course_code:

                    row['Code'] = updated_code
                    row['Name'] = updated_name
                    row['Credit'] = updated_credit
                    row['Pre-Requisite'] = updated_pre_requizite
                csv_writer.writerow(row)
        shutil.move(temp_file.name, 'course_data_updated.csv')

    @staticmethod
    def search_course(name, code):

        with open('course_data_updated.csv', 'r') as f:
            csv_reader = DictReader(f, lineterminator='\n')
            data = list(csv_reader)
            # print(data)
            for row in data:
                if row['Name'] == name or row['Code'] == code:
                    if row['Pre-Requisite'] == '':
                        nan = 'no Pre_Requisite'
                        print(
                            f'\n\t\tThis course exist in your Systrm \n \t Course Name: {row["Name"]} \n\t Course Code:  {row["Code"]} \n\t Course Credit: {row["Credit"]} \n\t {nan} \n')
                    else:
                        nan = row['Pre-Requisite']
                        print(
                            f'\n\t\tThis course exist in your Systrm \n \t Course Name: {row["Name"]} \n\t Course Code:  {row["Code"]} \n\t Course Credit: {row["Credit"]} \n\t {nan} \n')
                else:
                    print(
                        '\t\tThis course dosent exist \n \t\t please enter option (1) to add this course.')

    @staticmethod
    def check(name, code):

        with open('course_data_updated.csv', 'r') as file:

            csv_reader = DictReader(file, lineterminator='\n')
            for row in csv_reader:
                if row['Name'] == name or row['Code'] == code:
                    return True
                    '''print('this Course Exist\n')'''
                else:
                    return False

    @staticmethod
    def check2(name, code, pre_req):

        with open('course_data_updated.csv', 'r') as file:

            csv_reader = DictReader(file, lineterminator='\n')
            for row in csv_reader:
                if row['Pre-Requisite'].split() == pre_req:
                    return True
                    '''print('this Course Exist\n')'''
                else:
                    return False
