

def read_grades(filename):
    
    grades = {}
    with open(filename, 'r') as file:
        for line in file:
            name, grade = line.strip().split(',')
            grades[name] = int(grade)
    return grades

def calculate_statistics(grades):
    
    total_students = len(grades)
    total_sum = sum(grades.values())
    average = total_sum / total_students

    highest_grade = max(grades.values())
    lowest_grade = min(grades.values())

    passing = sum(1 for g in grades.values() if g >= 50)
    failing = total_students - passing

    grade_distribution = {
        'A': sum(1 for g in grades.values() if g >= 80),
        'B': sum(1 for g in grades.values() if 70 <= g < 80),
        'C': sum(1 for g in grades.values() if 60 <= g < 70),
        'D': sum(1 for g in grades.values() if 50 <= g < 60),
        'F': sum(1 for g in grades.values() if g < 50),
    }

    return average, highest_grade, lowest_grade, passing, failing, grade_distribution

def write_results(filename, statistics):
    
    average, highest, lowest, passing, failing, distribution = statistics
    with open(filename, 'w') as file:
        file.write(f"Average Grade: {average:.2f}\n")
        file.write(f"Highest Grade: {highest}\n")
        file.write(f"Lowest Grade: {lowest}\n")
        file.write(f"Passing Students: {passing}\n")
        file.write(f"Failing Students: {failing}\n")
        file.write("Grade Distribution:\n")
        for grade, count in distribution.items():
            file.write(f"  {grade}: {count}\n")


input_file = "grades.txt"
output_file = "grade_summary.txt"

grades_data = read_grades(input_file)
statistics = calculate_statistics(grades_data)
write_results(output_file, statistics)

print("Grade analysis complete. Results saved to", output_file)
