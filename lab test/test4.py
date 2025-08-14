import csv
import os

def read_student_data(csv_file_path):
    """Read CSV file containing student names and marks in 3 subjects."""
    students = []
    
    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            
            # Read header row
            header = next(csv_reader)
            print(f"Columns found: {', '.join(header)}")
            
            # Check if we have enough columns (Name + 3 subjects)
            if len(header) < 4:
                print("Error: CSV must have at least 4 columns (Name + 3 subjects)")
                return []
            
            # Read student data rows
            for row_num, row in enumerate(csv_reader, start=2):
                if len(row) != len(header):
                    print(f"Warning: Row {row_num} has {len(row)} columns, expected {len(header)}")
                    continue
                
                try:
                    # Extract student name and marks
                    student_name = row[0].strip()
                    marks = [float(mark.strip()) for mark in row[1:4]]  # First 3 subjects only
                    
                    # Calculate total and average
                    total_marks = sum(marks)
                    average_marks = round(total_marks / len(marks), 2)
                    
                    # Create student record
                    student = {
                        'name': student_name,
                        'marks': marks,
                        'total': total_marks,
                        'average': average_marks
                    }
                    
                    students.append(student)
                    
                except ValueError as e:
                    print(f"Warning: Row {row_num} has invalid marks: {e}")
                    continue
            
            print(f"Successfully loaded {len(students)} students")
            return students
            
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found!")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def display_results(students):
    """Display student results in a formatted table."""
    if not students:
        print("No student data to display!")
        return
    
    print("\n" + "="*60)
    print("STUDENT RESULTS")
    print("="*60)
    
    # Print header
    print(f"{'Name':<20} {'Subject 1':<10} {'Subject 2':<10} {'Subject 3':<10} {'Total':<8} {'Average':<8}")
    print("-"*60)
    
    # Print each student's data
    for student in students:
        marks_str = " ".join(f"{mark:<10}" for mark in student['marks'])
        print(f"{student['name']:<20} {marks_str} {student['total']:<8} {student['average']:<8}")
    
    print("-"*60)

def display_statistics(students):
    """Display class statistics."""
    if not students:
        return
    
    print("\n" + "="*40)
    print("CLASS STATISTICS")
    print("="*40)
    
    # Calculate overall statistics
    total_students = len(students)
    all_totals = [student['total'] for student in students]
    all_averages = [student['average'] for student in students]
    
    overall_average = round(sum(all_averages) / len(all_averages), 2)
    highest_total = max(all_totals)
    lowest_total = min(all_totals)
    highest_average = max(all_averages)
    lowest_average = min(all_averages)
    
    print(f"Total Students: {total_students}")
    print(f"Overall Class Average: {overall_average}%")
    print(f"Highest Total: {highest_total}")
    print(f"Lowest Total: {lowest_total}")
    print(f"Highest Average: {highest_average}%")
    print(f"Lowest Average: {lowest_average}%")

def create_sample_csv(filename="students.csv"):
    """Create a sample CSV file for testing."""
    sample_data = [
        ['Name', 'Mathematics', 'Science', 'English'],
        ['Alice Johnson', '85', '92', '78'],
        ['Bob Smith', '92', '88', '85'],
        ['Carol Davis', '78', '95', '90'],
        ['David Wilson', '88', '82', '88'],
        ['Emma Brown', '95', '89', '92']
    ]
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(sample_data)
        print(f"Sample CSV file '{filename}' created successfully!")
        print("Sample data includes 5 students with marks in Mathematics, Science, and English")
    except Exception as e:
        print(f"Error creating sample file: {e}")

def main():
    """Main function to run the student grade calculator."""
    print("�� STUDENT GRADE CALCULATOR")
    print("="*50)
    
    # Ask if user wants to create a sample CSV
    print("\nDo you want to create a sample CSV file for testing?")
    choice = input("Enter 'y' for yes, any other key for no: ").strip().lower()
    
    if choice == 'y':
        filename = input("Enter filename (default: students.csv): ").strip()
        if not filename:
            filename = "students.csv"
        create_sample_csv(filename)
        print()
    
    # Get CSV file path from user
    while True:
        csv_file = input("\nEnter the path to your CSV file: ").strip()
        
        # Remove quotes if user included them
        csv_file = csv_file.strip('"\'')
        
        if not csv_file:
            print("Please enter a valid file path!")
            continue
        
        if os.path.exists(csv_file):
            break
        else:
            print(f"File '{csv_file}' not found! Please check the path.")
    
    # Read and process student data
    students = read_student_data(csv_file)
    
    if students:
        # Display results
        display_results(students)
        
        # Display statistics
        display_statistics(students)
        
        print("\n✅ Analysis complete!")
    else:
        print("❌ No data could be processed. Please check your CSV file format.")

if __name__ == "__main__":
    main()