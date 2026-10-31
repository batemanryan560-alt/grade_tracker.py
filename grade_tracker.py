"""grade tracker: reads student data from a CSV and writes a class report."""

import csv

def load_students(filepath):
    """Read the CSV at filepath and return a list of student dictionaries."""
    students = []

    try:
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        print(f"Error: could not find the file '{filepath}'.")
        return []

    return students


def calculate_average(grades):
    """Return the average of a list of grades, or None if there are none."""
    valid = []

    for grade in grades:
        if grade.strip() == "":
            continue
        valid.append(float(grade))

    if len(valid) == 0:
        return None

    return round(sum(valid) / len(valid), 1)


def get_letter_grade(average):
    """Return the letter grade for a numeric average, or 'N/A' if None."""
    if average is None:
        return "N/A"
    elif average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"



def generate_report(students):
    """Return a summary dictionary for the full student list."""
    grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0, "N/A": 0}
    results = []
    averages = []

    for student in students:
        grades = [
            student["math"],
            student["science"],
            student["english"],
            student["history"],
        ]
        average = calculate_average(grades)
        letter = get_letter_grade(average)

        results.append({
            "name": student["student_name"],
            "average": average,
            "letter": letter,
        })

        grade_distribution[letter] += 1

        if average is not None:
            averages.append(average)

    results_sorted = sorted(results, key=lambda s: s["average"] or 0, reverse=True)

    return {
        "total_students": len(students),
        "class_average": round(sum(averages) / len(averages), 1) if averages else None,
        "highest_average": max(averages) if averages else None,
        "lowest_average": min(averages) if averages else None,
        "grade_distribution": grade_distribution,
        "students": results,
        "top_students": results_sorted[:5],
    }



def write_report(report, filepath):
    """Write the formatted report to a text file."""
    with open(filepath, "w") as file:
        file.write("=== Grade Report ===\n")
        file.write(f"Total students: {report['total_students']}\n")
        file.write(f"Class average: {report['class_average']}\n")
        file.write(f"Highest average: {report['highest_average']}\n")
        file.write(f"Lowest average: {report['lowest_average']}\n")

        file.write("\nGrade Distribution:\n")
        for letter, count in report["grade_distribution"].items():
            file.write(f"  {letter}: {count}\n")

        file.write("\nIndividual Results:\n")
        for student in report["students"]:
            file.write(f"  {student['name']:<20} {student['average']} ({student['letter']})\n")



def main():
    """Run the program: load data, generate a report, and write it out."""
    print("Loading student data...")
    students = load_students("data/students.csv")

    if not students:
        print("No student data loaded. Exiting.")
        return

    print(f"  Loaded {len(students)} students.")
    print()
    print("Generating report...")

    report = generate_report(students)

    print()
    print("--- Summary ---")
    print(f"Total students:   {report['total_students']}")
    print(f"Class average:    {report['class_average']}")
    print(f"Highest average:  {report['highest_average']}")
    print(f"Lowest average:   {report['lowest_average']}")
    print()
    print("Grade Distribution:")
    for letter, count in report["grade_distribution"].items():
        print(f"  {letter}: {count}")

    print()
    print("Top 5 students:")
    for student in report["top_students"]:
        print(f"  {student['name']:<20} {student['average']:<6} ({student['letter']})")

    print()
    write_report(report, "grade_report.txt")
    print("Report written to grade_report.txt")


if __name__ == "__main__":
    main()
