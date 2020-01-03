import statistics

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
class Course:
    def __init__(self, name):
        self.course_name = name
        self.students = []
    def add_student(self, name, grade):
        self.students.append(Student(name, grade))
    def class_avg(self):
        return statistics.mean([s.grade for s in self.students])

c = Course("Biostat 707")
print(c.course_name)
print(c.students)

c.add_student('Alex', 3.6)
c.add_student('Halley', 3.9)
print(c.class_avg())

b = Course('Biology')
b.add_student('David', 4.0)

print([student.grade for student in c.students])