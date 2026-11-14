
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


