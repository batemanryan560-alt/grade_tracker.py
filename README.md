\# Grade Tracker



A command-line Python program that reads student grades from a CSV file and writes a formatted class report.



\## Setup



No external packages are required. This project uses only Python's built-in `csv` module.



1\. Make sure Python 3 is installed.

2\. No installation step is needed — `requirements.txt` is empty on purpose.



\## Usage



From the project folder, run:



&#x20;   python grade\_tracker.py



The program reads `data/students.csv`, prints a summary to the terminal, and writes `grade\_report.txt`.



\## Project structure



&#x20;   grade-tracker/

&#x20;   ├── data/

&#x20;   │   └── students.csv

&#x20;   ├── grade\_tracker.py

&#x20;   ├── grade\_report.txt

&#x20;   ├── README.md

&#x20;   └── requirements.txt



\## Input format



`data/students.csv` has this structure:



&#x20;   student\_name,math,science,english,history

&#x20;   Alice Johnson,92,88,95,91



Some grade values may be missing (blank). The program skips them and averages only the grades that exist.



\## Functions



\- `load\_students(filepath)` — reads the CSV, returns a list of student dictionaries

\- `calculate\_average(grades)` — returns the average, skipping blank grades

\- `get\_letter\_grade(average)` — converts an average to a letter grade

\- `generate\_report(students)` — builds the summary dictionary

\- `write\_report(report, filepath)` — writes the formatted report to a text file



