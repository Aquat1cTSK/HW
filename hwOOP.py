class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and grade in range(11):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def a_grade(self):
        sum = 0
        i = 0
        for keys, values in self.grades.items():
            for valuess in values:
                sum += valuess
                i += 1
        average = sum / i
        return average

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Студент не в списке')
            return
        if self.a_grade() < other.a_grade():
            print(f'Успеваемость студента {other.name} лучше, чем у {self.name} ')
        elif self.a_grade() == other.a_grade():
            print(f'Успеваемость студента {other.name} идентична {self.name} ')
        else:
            print(f'Успеваемость студента {self.name} лучше, чем у {other.name} ')
        return self.a_grade() < other.a_grade()

    def __str__(self):
        res = f'Name : {self.name} \nSurname : {self.surname} \nAverage grade : {self.a_grade()} \nCourses in progress : {self.courses_in_progress} \nfinished courses : {self.finished_courses}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):

    def a_grade(self):
        sum = 0
        i = 0
        for keys, values in self.grades.items():
            for valuess in values:
                sum += valuess
                i += 1
        average = sum / i
        return average

    def __str__(self):
        res = f'Name : {self.name} \nSurname : {self.surname} \nAverage grade : {self.a_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Лектор не в списке')
            return
        else:
            if self.a_grade() < other.a_grade():
                print(f'Средний бал преподователя {other.name} лучше, чем у {self.name} ')
            elif self.a_grade() == other.a_grade():
                print(f'Средний бал преподователя {other.name} идентичен {self.name} ')
            else:
                print(f'Средний бал преподователя {self.name} лучше, чем у {other.name} ')

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if grade in range(11):
            if isinstance(student,
                          Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Name : {self.name} \nSurname : {self.surname}'
        return res

best_student = Student('Elizaveta', 'Kazarinskova', 'female')
best_student.courses_in_progress += ['Python']

not_best_student = Student('York', 'Stark', 'male')
not_best_student.courses_in_progress += ['Python']

first_reviewer = Reviewer('Sergei', 'Gromov')
first_reviewer.courses_attached += ['Python']

second_reviewer = Reviewer('Pavel', 'Lebed')
second_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Viktor', 'Dimov')
cool_lecturer.courses_attached += ['Python']

not_cool_lecturer = Lecturer('Petr', 'Ivanov')
not_cool_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(not_cool_lecturer, 'Python', 5)

not_best_student.rate_lecturer(cool_lecturer, 'Python', 10)
not_best_student.rate_lecturer(not_cool_lecturer, 'Python', 5)

first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(not_best_student, 'Python', 5)

second_reviewer.rate_hw(best_student, 'Python', 10)
second_reviewer.rate_hw(not_best_student, 'Python', 5)

list_student = [best_student, not_best_student]
list_lecturer = [cool_lecturer, not_cool_lecturer]

def average_grade_students(list_student, course):
    sum = 0
    i = 0
    for student in list_student:
        for grades in student.grades[course]:
            if course in student.grades:
                sum += grades
                i += 1
    res = sum / i
    return print(f'Средняя оценка студентов на курсе {course} равна {res}')

def average_grade_lecturer(list_lecturer, course):
    sum = 0
    i = 0
    for lecturer in list_lecturer:
        for grades in lecturer.grades[course]:
            if course in lecturer.grades:
                sum += grades
                i += 1
    res = sum / i
    return print(f'Средняя оценка лекторов на курсе {course} равна {res}')

print(best_student)
