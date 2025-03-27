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
    """Process the student data file and generate the output file without a header."""
    output_file = input_file + "_out.csv"
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        try:
            # Read the first row
            first_row = next(reader)
            # Check if it's a header (second column is not a digit)
            if not first_row[1].isdigit():
                # Header detected, skip it
                pass
            else:
                # No header, process the first row as data
                student_id = first_row[0]
                marks = [int(mark) for mark in first_row[1:] if mark.strip() != '']
                if marks:  # Only process if there are valid marks
                    average = sum(marks) / len(marks)
                    classification = calculate_classification(average)
                    writer.writerow([student_id, f"{average:.2f}", classification])
            
            # Process remaining rows
            for row in reader:
                if row:  # Skip empty rows
                    student_id = row[0]
                    marks = [int(mark) for mark in row[1:] if mark.strip() != '']
                    if marks:  # Only process if there are valid marks
                        average = sum(marks) / len(marks)
                        classification = calculate_classification(average)
                        writer.writerow([student_id, f"{average:.2f}", classification])
        except StopIteration:
            # Handle empty file gracefully
            pass

def main():
    """Main function to get the filename and process the data."""
    input_file = input("Enter the filename of the student file: ")
    process_student_data(input_file)
    print(f"Output written to {input_file}_out.csv")

if __name__ == "__main__":
    main()

