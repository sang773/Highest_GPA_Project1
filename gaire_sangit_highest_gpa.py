class Student:
    def __init__(self,first_name,last_name,gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa
    
    def get_first(self):
        return self.first_name
    
    def get_last(self):
        return self.last_name
    
class Course:
    def __init__(self):
        self.roster = []

    def add_student(self, student):
        self.roster.append(student)

    def course_size(self):
        return len(self.roster)
    
    def find_student_highest_gpa(self):
        if not self.roster:
            raise EmptyRosterError()

        highest_gpa_student = max(self.roster, key=lambda x: x.get_gpa())
        return highest_gpa_student
  
class EmptyRosterError(Exception):
    def __init__(self, message="Exception: Course Roster is Empty"):
        self.message = message
        super().__init__(self.message)

def validate_first_name(first_name):
    while not first_name:
        print("Please enter a valid first name.!!!")
        first_name = input("Enter First Name: ").strip()
    return first_name

def validate_last_name(last_name):
    while not last_name:
        print("Please enter a valid last name.!!!")
        last_name = input("Enter Last Name: ").strip()
    return last_name

def validate_gpa():
    while True:
        try:
            gpa = float(input("Enter GPA: "))
            if 0.0 <= gpa <= 4.0:
                return gpa
            else:
                print("Error: GPA should be between 0.0 and 4.0")
        except ValueError:
            print("Error: Please enter a numeric GPA between 0.0 and 4.0")

def user_inputs():
    students = []
    while True:
        first_name = validate_first_name(input("Enter the First Name (Type 'quit' or 'q' to exit): ").strip())
        if first_name.lower() in {'quit', 'q'}:
            break
        
        last_name = validate_last_name(input("Enter the Last Name: ").strip())
        gpa = validate_gpa()

        print()
        student = Student(first_name, last_name, gpa)
        students.append(student)

    return students


def main():
    print()
    print("Welcome to CSC/DSCI 1301: Principles in CS/DS 1")
    print("Please Add Students to the Course: (quit or q to exit).")
    print()
    course = Course()

    students = user_inputs()
    for student in students:
        course.add_student(student)

    num_students = course.course_size()
    try:
        highest_gpa_student = course.find_student_highest_gpa()
        highest_gpa = highest_gpa_student.get_gpa()
        highest_first_name = highest_gpa_student.get_first()
        highest_last_name = highest_gpa_student.get_last()
        print()
        print(f"Course Size: {num_students} students")
        print(f"Top student: {highest_first_name} {highest_last_name} ( GPA: {highest_gpa} )")
        print()
    except EmptyRosterError as e:
        print()
        print("Course Size: 0 students")
        print(e)

if __name__ == "__main__":
    main()
        



    










    
    

