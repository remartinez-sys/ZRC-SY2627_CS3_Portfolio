class Course:
    def __init__(self, course_id: str, title: str):
        self.course_id = course_id
        self.title = title
        self.students = []

    def add_student(self, student: 'Student'):
        if student not in self.students:
            self.students.append(student)
            print(f"Added {student.name} to {self.title}.")

    def get_students(self):
        return self.students


class Student:
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name

    def enrollInCourse(self, course: Course):
        # Calls the course's method to add this student to its list
        course.add_student(self)


# --- Testing the code ---
# Changed names and course details
student1 = Student("S2024-01", "Leo")
course1 = Course("BIO101", "Foundations of Biology")

# Option 1: Enroll directly through the course
course1.add_student(student1)

# Option 2: Enroll through the student (like your original code)
student2 = Student("S2024-02", "Mia")
student2.enrollInCourse(course1)

print("\n--- Enrolled Students ---")
for student in course1.get_students():
    print(f"Student ID: {student.student_id}, Name: {student.name}")