class AssignmentSubmission:

  def __init__(
      self,
      student_name: str,
      student_id: str,
      assignment_title: str,
      due_date: str,
  ):
   
    self.student_name: str = student_name
    self.student_id: str = student_id

    
    self._assignment_title: str = assignment_title
    self._due_date: str = due_date

    
    self.__is_submitted: bool = False
    self.__submitted_file: list[str] = []
    self.__score: float = -1.0 

  

  def __validate_grade(self, score: float) -> bool:
  
    return 0.0 <= score <= 100.0

  def __check_submission_status(self) -> bool:
   
    self.__is_submitted = len(self.__submitted_file) > 0
    return self.__is_submitted

  def __is_duplicate(self, filename: str) -> bool:
   
    return filename in self.__submitted_file

  

  def add_file(self, filename: str):
   
    if self.__is_duplicate(filename):
      print(f"[Error] File '{filename}' already exists.")
    else:
      self.__submitted_file.append(filename)
      self.__check_submission_status()
      print(f"[Success] Added file: {filename}")

  def remove_file(self, filename: str):
    
    if filename in self.__submitted_file:
      self.__submitted_file.remove(filename)
      self.__check_submission_status()
      print(f"[Success] Removed file: {filename}")
    else:
      print(f"[Error] File '{filename}' not found.")

  def assign_grade(self, score: float):
    
    if not self.__is_submitted:
      print("[Error] Cannot grade an unsubmitted assignment.")
    elif self.__validate_grade(score):
      self.__score = score
      print(f"[Success] Grade of {score} assigned to {self.student_name}.")
    else:
      print("[Error] Invalid score. Must be between 0.0 and 100.0.")

  def get_grade(self) -> str:

    if self.__score == -1.0:
      return "Ungraded"
    return f"{self.__score}/100"

  def view_files(self) -> str:
    
    if not self.__submitted_file:
      return "No files uploaded."
    return ", ".join(self.__submitted_file)

  def get_status_report(self) -> str:
   
    return (
        f"--- Status Report ---\n"
        f"Student: {self.student_name} ({self.student_id})\n"
        f"Assignment: {self._assignment_title}\n"
        f"Due Date: {self._due_date}\n"
        f"Submitted: {self.__is_submitted}\n"
        f"Files: {self.view_files()}\n"
        f"Grade: {self.get_grade()}\n"
        f"---------------------"
    )


student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id= "pshs-1090-x", assignment_title= "CS-101", due_date= "2026-10-15")
student1.add_file("main.py")
student1.remove_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95.0)

print(f"Alex's file: {student1.view_files()}")

