import csv

def classify_grade(average):
    """Classifies a student's average grade according to the given boundaries."""
    if average >= 70:
        return "1"
    elif average >= 60:
        return "2:1"
    elif average >= 50:
        return "2:2"
    elif average >= 40:
        return "3"
    else:
        return "F"

def process_student_data(filename):
    """Reads student data, calculates their average grades and classifications, then writes output to a new CSV file."""
    output_filename = filename.replace(".csv", "_out.csv")

    with open(filename, newline='') as infile, open(output_filename, "w", newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Read header row and ignore
        header = next(reader)

        # Write the new header for the output file
        writer.writerow(["student_id", "average_grade", "classification"])

        for row in reader:
            student_id = row[0]  # First column is always student_id
            grades = [int(grade) for grade in row[1:] if grade]  # Convert valid grades to integers

            if grades:
                average_grade = sum(grades) / len(grades)
                classification = classify_grade(average_grade)
                writer.writerow([student_id, f"{average_grade:.2f}", classification])

    print(f"Processing complete! Output saved to {output_filename}")

# Prompt user for the filename
filename = input("Enter the student data filename (e.g., student_data_10.csv): ").strip()
process_student_data(filename)

