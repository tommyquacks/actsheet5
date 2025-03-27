import csv

def calculate_classification(average):
    """Determine the classification based on the average grade."""
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

def process_student_data(input_file):
    """Process the student data file and generate the output file."""
    output_file = input_file + "_out.csv"
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write the output header
        writer.writerow(["student_id", "average_grade", "classification"])

        # Check and skip header
        try:
            first_row = next(reader)
            try:
                int(first_row[1])  # Try converting second element to int
                # It's a data row – process it
                rows = [first_row] + list(reader)  # Include first_row + rest
            except ValueError:
                # It's a header – skip it
                rows = list(reader)
        except StopIteration:
            # File is empty
            return

        # Process all data rows
        for row in rows:
            student_id = row[0]
            marks = [int(mark) for mark in row[1:] if mark.strip() != '']
            if marks:
                average = sum(marks) / len(marks)
                classification = calculate_classification(average)
                writer.writerow([student_id, f"{average:.2f}", classification])

def main():
    """Main function to ask for the filename and process the data."""
    input_file = input("Enter the filename of the student file: ")
    process_student_data(input_file)
    print(f"Output written to {input_file}_out.csv")

if __name__ == "__main__":
    main()

