class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = int()

    def add_corses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f"Имя: {self.name}\nФамилия: {self.surname}\n" \
                 f"Средняя оценка за домашние задания: {self.average_grades}\n" \
                 f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
                 f"Завершенные курсы: {','.join(self.finished_courses)}"
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Students')
            return
        return self.average_grades < other.average_grades

    def average_rating(self, students, course) -> None:
        for student in students:
            result = sum(student.grades.get(course)) / len(student.grades.get(course))
            student.average_grades = result


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    average_grades: float

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades = float()

    def calculation_of_average_grades(self, lecturers, course):
        for lecturer in lecturers:
            result = sum(lecturer.grades.get(course)) / len(lecturer.grades.get(course))
            lecturer.average_grades = result
        return

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                 f'Средняя оценка за лекции: {self.average_grades}'
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.average_grades < other.average_grades


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


# Создаем экземпляры класса Student
mihailov = Student('Some', 'Buddy', 'Мужчина')
mihailov.courses_in_progress += ['Python']
rudakov = Student('Some', 'Buddy', 'Мужчина')
rudakov.courses_in_progress += ['Python']
rudakov.courses_in_progress += ['GIT']

# Создаем экземпляры класса Lecturer
lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Some', 'Buddy')
lecturer_2.courses_attached += ['Python']

# Создаем экземпляры класса Reviewer
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Some', 'Buddy')
reviewer_2.courses_attached += ['Python']

# Добавляем оценки студентам за курс Python
reviewer_1.rate_hw(mihailov, 'Python', 10)
reviewer_1.rate_hw(rudakov, 'Python', 9)
reviewer_2.rate_hw(mihailov, 'Python', 7)
reviewer_2.rate_hw(rudakov, 'Python', 10)

# Добавляем оценки лекторам за курс Python
mihailov.rate_lecture(lecturer_1, 'Python', 7)
mihailov.rate_lecture(lecturer_2, 'Python', 9)
rudakov.rate_lecture(lecturer_1, 'Python', 10)
rudakov.rate_lecture(lecturer_2, 'Python', 10)

# Добавляем пройденный курс студенту
mihailov.add_corses('Введение в программирование')

# Рассчитываем средние оценки для студентов за курс Python
Student.average_rating([rudakov, mihailov], 'Python')

# Рассчитываем средние оценки для лекторов за курс Python
Lecturer.calculation_of_average_grades([lecturer_1, lecturer_2], 'Python')

# Проверяем переопределенные методы для созданных классов
print(reviewer_1, end='\n\n')
print(lecturer_1, end='\n\n')
print(lecturer_2, end='\n\n')
print(lecturer_1 > lecturer_2, end='\n\n')
print(rudakov, end='\n\n')
print(mihailov, end='\n\n')
print(rudakov > mihailov, end='\n\n')
