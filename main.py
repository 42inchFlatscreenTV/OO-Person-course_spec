class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printFullName(self):
        print(f"Full Name: {self.first_name} {self.last_name}")

class Student(Person):
    def __init__(self, first_name, last_name, student_id, houseGroup, subjects):
        super().__init__(first_name, last_name)
        self.student_id = student_id
        self.houseGroup = houseGroup
        self.subjects = []

    def enrolClass(self, subjectName):
        s1 = Subject(subjectName)
        s1.subjectName = subjectName
        s1.student_id = self.student_id

        self.subjects.append(s1)
        return
    
    def showSubjects(self):
        print(self.subjects)
        return
    
class Subject:
    def __init__(self, student_id, subjectName):
        self.subjectName = subjectName
        self.student_id = student_id

    def printStudentList(self):
        return
    
class Parent(Person):
    def __init__(self, first_name, last_name, occupation, alumni):
        super().__init__(first_name, last_name)
        self.soccupation = occupation
        self.alumni = alumni

