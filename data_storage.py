# Defined Semester 1 subjects (using a set)
SEM_1_SUBJECTS = ("Calculus", "Python", "English", "EVS")

# Dictionary to hold all student records
# Format: { roll_no: {"name": str, "marks": {subject: score}} }
students = {}

# Helper function to add a new student record
def add_stud(roll_no: str, name: str, marks: dict = None):
    """
    Adds a student record to the students dictionary.
    """
    if marks is None:
        marks = {}
    students[roll_no] = {
        "name": name,
        "marks": marks
    }