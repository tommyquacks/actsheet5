import csv

def classify_grade(grade):
    grade = float(grade)
    if grade >= 70:
        return '1st'
    elif grade >= 60:
        return '2:1'
    elif grade >= 50:
        return '2:2'
    elif grade >= 40:
        return '3rd'
    else:
        return 'F'

# Read input CSV (assumed to include a header)
with open('input.csv', 'r') as infile:
    reader = csv.reader(infile)
    header = next(reader)  # Skip the header row

    results = []  # This will store the output rows

    for row in reader:
        student_id = row[0]
        grades = list(map(float, row[1:]))
        avg = round(sum(grades) / len(grades), 2)
        classification = classify_grade(avg)
        results.append([student_id, f"{avg:.2f}", classification])

# Write output CSV
with open('output.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    # Write header once
    writer.writerow(['student_id', 'average_grade', 'classification'])
    # Write student data
    writer.writerows(results)
