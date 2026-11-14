
# НАСЛЕДОВАНИЕ

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} # оценки

    #  str
    def _average_grade(self):
        all_grades = [g for grades in self.grades.values() for g in grades]
        if not all_grades:
            return 0
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self._average_grade()}"
        )

    # сравнениепо средней оценке

    def __eq__(self, other):
        return self._average_grade() == other._average_grade()

    def __lt__(self, other):
        return self._average_grade() < other._average_grade()

    def __le__(self, other):
        return self._average_grade() <= other._average_grade()


# Reviewer
class Reviewer(Mentor):

    # Reviewer выставляет оценки за ДЗ

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    # str
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# Класс Student
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}   # оценки за ДЗ (ставит Reviewer)

    # студент ставит оценки лекторам
    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return "Ошибка"
        if course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    # средние оценки за ДЗ
    def _average_hw(self):
        all_grades = [g for grades in self.grades.values() for g in grades]
        if not all_grades:
            return 0
        return round(sum(all_grades) / len(all_grades), 1)

    # str
    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self._average_hw()}\n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}"
        )

    # студенты по средней оценке за ДЗ
    def __eq__(self, other):
        return self._average_hw() == other._average_hw()

    def __lt__(self, other):
        return self._average_hw() < other._average_hw()

    def __le__(self, other):
        return self._average_hw() <= other._average_hw()


# task4: средняя за ДЗ по курсу
def average_hw_by_course(students, course):
    total = []
    for student in students:
        if course in student.grades:
            total.extend(student.grades[course])
    if not total:
        return 0
    return round(sum(total) / len(total), 1)


def average_lecture_by_course(lecturers, course):
    total = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total.extend(lecturer.grades[course])
    if not total:
        return 0
    return round(sum(total) / len(total), 1)


# task4. СОЗДАНИЕ ЭКЗЕМПЛЯРОВ


lecturer1 = Lecturer("Иван", "Иванов")
lecturer2 = Lecturer("Сергей", "Смирнов")

reviewer1 = Reviewer("Пётр", "Петров")
reviewer2 = Reviewer("Анна", "Кузнецова")

student1 = Student("Алёхина", "Ольга", "Ж")
student2 = Student("Дмитрий", "Соколов", "М")

# курсы
lecturer1.courses_attached += ["Python", "Java"]
lecturer2.courses_attached += ["Python", "C++"]

reviewer1.courses_attached += ["Python", "C++"]
reviewer2.courses_attached += ["Python", "Java"]

student1.courses_in_progress += ["Python", "Java"]
student1.finished_courses += ["Введение в программирование"]

student2.courses_in_progress += ["Python", "C++"]
student2.finished_courses += ["Git"]
