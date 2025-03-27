import csv
import os

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
        # Write the header to the output file
        writer.writerow(["student_id", "average_grade", "classification"])
        
        for row in reader:
            student_id = row[0]
            # Extract module marks, ignoring empty strings
            marks = [int(mark) for mark in row[1:] if mark.strip() != '']
            if marks:
                # Calculate average
                average = sum(marks) / len(marks)
                # Determine classification
                classification = calculate_classification(average)
                # Write to output file with average formatted to 2 decimal places
                writer.writerow([student_id, f"{average:.2f}", classification])

def main():
    """Main function to ask for the filename and process the data."""
    input_file = input("Enter the filename of the student file: ")
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return
    process_student_data(input_file)
    print(f"Output written to {input_file}_out.csv")

if __name__ == "__main__":
    main()
