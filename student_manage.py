from data_storage import students, SEM_1_SUBJECTS
from testing import get_valid_score


def add_new_stud(roll_no, name):
    """Adds a new student entry to data_store."""
    if roll_no in students:
        print("[!] A student with this Roll Number already exists.")
        return False
    
    students[roll_no] = {
        "name": name,
        "marks": {}
    }
    print(f"Student '{name}' has been added successfully.")
    return True

def enter_marks(roll_no):
    """Prompts for marks in Calculus, Python, English, and EVS."""
    if roll_no not in students:
        print("[!] Roll Number not found.")
        return

    print(f"\nEntering Marks for {students[roll_no]['name']}:")
    for subject in SEM_1_SUBJECTS:
        score = get_valid_score(f"  Enter mark for {subject} (0-100): ")
        students[roll_no]["marks"][subject] = score

    print(f"All 4 subject marks are saved for Roll No: {roll_no}")