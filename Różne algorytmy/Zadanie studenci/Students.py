class Student():
    def __init__(self,name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_avg(self):
        return round(sum(self.grades)/len(self.grades))
