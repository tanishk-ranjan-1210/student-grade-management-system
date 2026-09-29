from data_storage import students, SEM_1_SUBJECTS
from grade_calc import calc_total, calc_percent, grade_calc

def give_reportcard(roll_no):
    """Prints a report card which is being formatted by the module."""
    if roll_no not in students:
        print("[!] Roll Number not found.")
        return
        
    student = students[roll_no]
        
    if not student["marks"]:
        print("[!] Marks have not been entered for this student yet.")
        return
            
    total = calc_total(student["marks"])
    pct = calc_percent(total)
    grade = grade_calc(pct)
    
    print("\n" + "=" * 40)
    print("          SEMESTER 1 REPORT CARD          ")
    print("=" * 40)
    print(f" Roll Number : {roll_no}")
    print(f" Name        : {student['name']}")
    print("-" * 40)
    for sub, score in student["marks"].items():
        print(f" {sub:<12} : {score: .2f} / 100")
    print("-" * 40)
    print(f" Total Score : {total: .2f} / 400")
    print(f" Percentage  : {pct: .2f}%")
    print(f" Final Grade : {grade}")
    print("=" * 40 + "\n")