import numpy as np


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def get_avr_score(self):
        sum_score = 0
        counter = 0
        for score in self.grades.values():
            sum_score += sum(score)
            counter += len(score)
        return round(sum_score / counter, 2)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lectors(self, lector, course, grade):
        if isinstance(lector,
                      Lecturer) and course in lector.courses_attached and course in self.courses_in_progress and grade <= 10:
            lector.grades.append(grade)
        else:
            return "Ошибка"

    def __str__(self):
        white_students = f' \n Имя:{self.name}' \
                         f' \n Фамилия:{self.surname}' \
                         f' \n Средняя оценка за домашние задания :{self.get_avr_score()}' \
                         f' \n Курсы в процессе изучения:{self.courses_in_progress}' \
                         f' \n Завершенные курсы:{self.finished_courses}'
        return white_students

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'Студента нет')
            return
        else:
            compare = self.get_avr_score() < other.get_avr_score()
            if compare:
                print(f'Студент {self.name} {self.surname} учится хуже {other.name} {other.surname}')
            else:
                print(f'Студент {self.name} {self.surname} учится лучше {other.name} {other.surname}')
        return compare


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        white_mentors = f' \n Имя:{self.name}' f' \n Фамилия:{self.surname}'
        return white_mentors


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = []

    def __str__(self):
        white_lectors = f' \n Имя:{self.name}' \
                        f' \n Фамилия:{self.surname}' \
                        f' \n Средняя оценка за лекции:{np.mean(self.grades)}'
        return white_lectors

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return "Нет лектора"
        return np.mean(self.grades) < np.mean(other.grades)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        write_reviewers = f' \n Имя:{self.name}' \
                          f' \n Фамилия:{self.surname}'
        return write_reviewers


hulk = Student('Брюс', 'Беннер', 'мужской')
hulk.courses_in_progress += ['Физика']
hulk.finished_courses += ['Химия']

tor = Student('Тор', 'Одинов', 'мужской')
tor.courses_in_progress += ['Физика']
tor.finished_courses += ['Химия']

capitan = Reviewer('Стив', 'Роджерс')
capitan.courses_attached += ['Физика']
capitan.courses_attached += ['Химия']

ironman = Reviewer('Тони', 'Старк')
ironman.courses_attached += ['Химия']
ironman.courses_attached += ['Физика']

tanos = Lecturer('Танос', 'Титанов')
tanos.courses_attached += ['Химия']
tanos.courses_attached += ['Физика']

widow = Lecturer('Наташа', 'Романов')
widow.courses_attached += ['Физика']
widow.courses_attached += ['Химия']

ironman.rate_hw(tor, 'Физика', 8)
ironman.rate_hw(tor, 'Физика', 5)
ironman.rate_hw(tor, 'Физика', 9)

capitan.rate_hw(hulk, 'Физика', 7)
capitan.rate_hw(hulk, 'Физика', 3)
capitan.rate_hw(hulk, 'Физика', 8)

hulk.rate_lectors(tanos, 'Физика', 8)
hulk.rate_lectors(widow, 'Физика', 5)

tor.rate_lectors(tanos, 'Физика', 8)
tor.rate_lectors(widow, 'Физика', 4)


def get_avr_st_grade(student_list, course):
    sum_grade = 0
    for student in student_list:
        for key, value in student.grades.items():
            if key == course:
                sum_grade += sum(value) / len(value)
    return round(sum_grade / len(student_list), 2)


def get_avr_lec_grade(lector_list):
    sum_grades = 0
    for lecturer in lector_list:
        sum_grades += sum(lecturer.grades) / len(lecturer.grades)
    return round(sum_grades / len(lector_list), 2)
