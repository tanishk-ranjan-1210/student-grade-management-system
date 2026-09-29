# student-grade-management-system

## Project Overview

This is a Python project made to manage student marks and calculate their grades.It allows the user to add students, enter their Semester 1 marks, calculate their total and percentage, and generates a report card.

The project also shows basic class analytics such as the average percentage and the top scorer.

I made this project to make basic student result mmanagement easier and to practice Python concept like functions, dictionaries, modules, loops, conditions, and input validation.

## Features

- Add a new student using roll number and name.
- Checks if the roll number already exists.
- Takes marks for Semester 1 subjects.
- Checks that marks are between 0 and 100.
- Calculates total marks.
- Calculates percentage.
- Assigns a final grade.
- Generates a Semester 1 report card.
- Shows class average percentage.
- Shows the top scorer.
- Handles invalid marks and inavlid menu choices.
- Works completely through the terminal.

## Subjects

The project currently contains four Semester 1 subjects:

- Calculus
- Python
- English
- EVS

Each subject is marked out of 100.

## Technologies Used

- Python 3
- Python functions
- Python modules
- Dictionaries
- Loops and conditional statements
- Expection handling
- Git and GitHub for version control

No external Python libraries are required. 

## Project Structure

- 'main.py' - Main programm and menu
- 'data_storage.py' - Student data storage
- 'student_manage.py' - Student and marks management
- 'grade_calc.py' - Grade calculations
- 'creating_report.py' - Report generation
- 'stats.py' - Class statistics
- 'testing.py' - Input validation

## Installation

Install Python 3

## How to Run

Open the project folder in a terminal and run:

'''bash
pytho main.py

## Limitations
- The program works only in the terminal.
- Student data is stored only while the program is running.
- Data is lost when the program is closed.
- The project currently supports only four Semester 1 subjects.
- There is no database for permanent data storage.
- There is no graphical user interface.
- The current version does not include user login or authentication.

## Future Improvements

- Add permanent student data storage using a database or file.
- Add options to update and delete student records.
- Add support for multiple semesters.
- Add more detailed class and subject-wise analytics.
- Add a simple graphical user interface.
- Generate student report cards as PDF files.
- Add user login and authentication.
- Add data export to CSV or Excel.

### Written by Tanishk Ranjan.