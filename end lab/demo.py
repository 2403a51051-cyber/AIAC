"""
Demo script showing the Student class in action with output.
"""

from task1 import Student


print("=" * 70)
print("SMART ATTENDANCE APP - Student Class Demo")
print("=" * 70)

# Create a student object
student1 = Student("Ayesha", "22CSE31")
print(f"\nStudent Created: {student1.name} (Roll No: {student1.roll_no})")
print(f"Initial Attendance: {student1.attendance_percentage()}%")

# Mark attendance for multiple classes
print("\n--- Marking Attendance for Student 1 ---")
student1.mark_attendance(True)
print(f"Class 1 - Present | Total: {student1.total_classes}, Attended: {student1.attended_classes}, Percentage: {student1.attendance_percentage()}%")

student1.mark_attendance(True)
print(f"Class 2 - Present | Total: {student1.total_classes}, Attended: {student1.attended_classes}, Percentage: {student1.attendance_percentage()}%")

student1.mark_attendance(False)
print(f"Class 3 - Absent  | Total: {student1.total_classes}, Attended: {student1.attended_classes}, Percentage: {student1.attendance_percentage()}%")

student1.mark_attendance(True)
print(f"Class 4 - Present | Total: {student1.total_classes}, Attended: {student1.attended_classes}, Percentage: {student1.attendance_percentage()}%")

# Display final student details
print("\n--- Final Report for Student 1 ---")
print(student1)
print(f"Total Classes: {student1.total_classes}")
print(f"Classes Attended: {student1.attended_classes}")
print(f"Classes Absent: {student1.total_classes - student1.attended_classes}")

# Create another student
print("\n" + "=" * 70)
student2 = Student("Rajesh", "22CSE32")
print(f"\nStudent Created: {student2.name} (Roll No: {student2.roll_no})")

print("\n--- Marking Attendance for Student 2 ---")
for i in range(5):
    present = i != 2  # Absent on 3rd class
    student2.mark_attendance(present)
    status = "Present" if present else "Absent"
    print(f"Class {i+1} - {status:6} | Attendance: {student2.attendance_percentage()}%")

print("\n--- Final Report for Student 2 ---")
print(student2)
print("=" * 70)
