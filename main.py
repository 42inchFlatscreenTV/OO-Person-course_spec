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
        self.subjects.append(subjectName)
        subjectName.students.append(self)  # Add this student to the subject's student list

        return
    
    def showSubjects(self):
        print(self.subjects)
        return
    
class Subject:
    def __init__(self, subjectName):
        self.subjectName = subjectName
        self.students = []

    def printStudentList(self):
        for student in self.students:
            print(f"{student.first_name} {student.last_name}")

    
class Parent(Person):
    def __init__(self, first_name, last_name, occupation, alumni):
        super().__init__(first_name, last_name)
        self.soccupation = occupation
        self.alumni = alumni



if __name__ == "__main__":
    # Input for subjects
    subject_names = input("Enter subjects separated by commas: ").split(",")
    subjects = [Subject(name.strip()) for name in subject_names]

    # Input for student
    first_name = input("\nEnter student first name: ")
    last_name = input("\nEnter student last name: ")
    student_id = input("\nEnter student ID: ")
    house_group = input("\nEnter student house group: ")
    student1 = Student(first_name, last_name, student_id, house_group, [])

    # Enrol student in subjects
    print("\nAvailable subjects:")
    for idx, subj in enumerate(subjects):
        print(f"{idx + 1}: {subj.subjectName}")
    chosen = input("Enter subject numbers to enrol (comma separated): ").split(",")
    for idx in chosen:
        subj = subjects[int(idx.strip()) - 1]
        student1.enrolClass(subj)

    # Show student's subjects
    print("\nStudent's enrolled subjects:")
    student1.showSubjects()

    # Print student's full name
    student1.printFullName()

    # Print students in each subject
    for subj in subjects:
        print(f"---------------------------\nStudents in {subj.subjectName}:")
       
        subj.printStudentList()

    # Input for parent
    parent_first = input("---------------------------\n\nEnter parent first name: ")
    parent_last = input("\nEnter parent last name: ")
    occupation = input("\nEnter parent occupation: ")
    alumni = input("\nIs the parent an alumni? (yes/no): ").lower() == "yes"
    parent1 = Parent(parent_first, parent_last, occupation, alumni)
    parent1.printFullName()