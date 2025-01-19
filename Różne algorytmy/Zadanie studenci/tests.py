from Students import Student


def test_students_get_grade():
    student = Student("Marcin")
    assert student.name == "Marcin"
    assert student.grades == []
def test_students_add_grade():
    student = Student("Marcin")
    student.add_grade(5)
    assert student.grades == [5]

    student.add_grade(3)
    assert  student.grades == [5,3]
def test_students_get_avg():
    student = Student("Marcin")
    student.add_grade(5)
    student.add_grade(6)
    student.add_grade(4)
    assert  student.get_avg() == 5