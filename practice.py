

from subprocess import call


class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def speaks(self):
        print(self.name, ' saying how you doing')

    def biography(self):
        print(f'Name: {self.name} \n Occupation: {self.occupation}')


person_A = Human('Rifat Hossain', 'Machine Learning Engineer')
person_B = Human('Sifat Kaissa', 'Data Scientist')
person_A.speaks()
person_B.speaks()
person_A.biography()
person_B.biography()

# Inheritance


class Vehicle:
    def general_usage(self):  # self is must, or later on it will give error.
        print('commute to destination ')


class Car(Vehicle):
    def __init__(self):
        print('This is car')
        self.wheels = 4
        self.has_roofs = True

    def specific_usage(self):

        print('office work, family time, long commute')


class Motorcycle(Vehicle):
    def __init__(self):
        print('This is Motorcycle')
        self.wheels = 2
        self.has_roofs = False

    def specific_usage(self):
        print('riding, fun, short commute')
        self.general_usage()
# calling them these classes inharited general usage


class Animal:
    def __init__(self, name, bread, color, animal_category, sound):
        self.name = name
        self.bread = bread
        self.color = color
        self.animal_category = animal_category
        self.sound = sound

    def call(self):
        print(f'{self.animal_category} sounds like {self.sound}')

    def info(self):

        print(
            f'Name:{self.name}\nBread:{ self.bread}\nColor:{ self.color}\nAnimal Type: { self.animal_category}\n')
        self.call()


rolls_roice = Car()
rolls_roice.specific_usage()
rolls_roice.general_usage()
print('\n ')
S1000rr = Motorcycle()
S1000rr.specific_usage()
print('------------------------------------------')
tom = Animal('Tom', 'american', 'gray', 'cat', 'Meao')
tom.info()
print('\n ')
print('------------------------------------------')


class Dog(Animal):
    def __init__(self, name, bread, color, animal_category, sound, size, legs=4):
        super().__init__(name, bread, color, animal_category, sound)
        self.size = size
        self.legs = legs

    def info(self):
        super().info()
        print(f'size: {self.size}')


bull = Dog('bull', 'American', 'gray', 'Dog', 'gaw', 'Big')
bull.info()


while user_input != 6:
    for info in infos:
        print(f'{info}\n')
    user_input = int(input(
        'Select your input from these flowing options by pressing the SERIAL NUMBER \n6 EX (1,2,3,4,5,6) FROM 1 TO 6 AND ENTER\n'))
print(prompt)

# try:
# except ValueError:
#   print('Input error suggestion (inout these data in order)')
course_code = input(f'type {course}:')
course_prerequizite = input(f'type {course}:')
course_credit = input(f'type {course}:')
for courses in range(0, 4):
           if courses[0] == '':
                flag = 1
            if course[1] == '':
                flag += 2
            if course[2] == '':
                flag += 3
            if course[3] == '':
                flag += 4
            if flag == 7:
                print('enter these value again , pre_ requizite is not mendetory')




'''
elif Course.check2(courses[0], courses[1], courses[2]) == True:
                break
            else:
                Course.check2(courses[0], courses[1], courses[2]) == False
                while True:

                    field_input = input(
                        'would you like to enter pre_requisite ? y/n\n')
                    if field_input == 'y':
                        field_input = input(
                            'for every pre-requisite leave a space behind ,\n ex: mat100 mat200\n')
                        courses[2] = field_input
                        break
                    else:
                        courses[2] = 'nan'
                        break

'''