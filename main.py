from student_manage import add_new_stud, enter_marks
from creating_report import give_reportcard
from stats import show_stats

def main():
    while True:
        print("="*80)
        print(" "*20,"STUDENT GRADE MANAGEMENT SYSTEM ")
        print("="*80)
        print("1. Add New Student")
        print("2. Enter Subject Marks (Sem 1)")
        print("3. View Student Report Card")
        print("4. View Class Analytics")
        print("5. Exit")
        print("-"*40)

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            roll = input("Enter Roll Number (eg:26bce...): ").strip().lower()
            name = input("Enter Student Name: ").strip().lower()
            if roll and name:
                add_new_stud(roll, name)

        elif choice == "2":
            roll = input("Enter Roll Number: ").strip().lower()
            enter_marks(roll)

        elif choice == "3":
            roll = input("Enter Roll Number: ").strip().lower()
            give_reportcard(roll)

        elif choice == "4":
            show_stats()

        elif choice == "5":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("[!] Invalid choice. Please select 1 to 5.")

if __name__ == "__main__":
    main()