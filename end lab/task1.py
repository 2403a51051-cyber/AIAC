
"""
Task 1: Smart Attendance System using OOP in Python

This script defines a Student class to manage attendance.
Includes: Docstrings, inline comments, and simple unit tests.
"""

class Student:
    """
    Represents a student in a smart attendance app.

    Attributes:
        name (str): Name of the student.
        roll_no (str): Unique roll number.
        total_classes (int): Total classes conducted.
        attended_classes (int): Total classes attended.
    """

    def __init__(self, name, roll_no):
        """
        Initialize Student object.

        Args:
            name (str): Student Name
            roll_no (str): Student Roll Number
        """
        self.name = name
        self.roll_no = roll_no
        self.total_classes = 0
        self.attended_classes = 0

    def mark_attendance(self, present=True):
        """
        Mark attendance for a student.

        Args:
            present (bool): True if present, False if absent
        """
        self.total_classes += 1  # class counted whenever action happens
        if present:
            self.attended_classes += 1

    def attendance_percentage(self):
        """
        Calculate attendance percentage.

        Returns:
            float: percentage (0 if no classes conducted)
        """
        if self.total_classes == 0:
            return 0.0
        return round((self.attended_classes / self.total_classes) * 100, 2)

    def __str__(self):
        """Readable format of student details."""
        return f"{self.name} ({self.roll_no}) - Attendance: {self.attendance_percentage()}%"


# ----------------- UNIT TESTS -----------------
import unittest

class TestStudentAttendance(unittest.TestCase):

    def test_initial_state(self):
        student = Student("Ayesha", "22CSE31")
        self.assertEqual(student.total_classes, 0)
        self.assertEqual(student.attended_classes, 0)
        self.assertEqual(student.attendance_percentage(), 0.0)

    def test_present_attendance(self):
        student = Student("Ayesha", "22CSE31")
        student.mark_attendance(True)
        self.assertEqual(student.attendance_percentage(), 100.0)

    def test_absent_attendance(self):
        student = Student("Ayesha", "22CSE31")
        student.mark_attendance(False)
        self.assertEqual(student.attendance_percentage(), 0.0)

    def test_percentage_calculation(self):
        student = Student("Ayesha", "22CSE31")
        student.mark_attendance(True)
        student.mark_attendance(True)
        student.mark_attendance(False)
        self.assertEqual(student.attendance_percentage(), 66.67)


# -------------- Example usage output --------------
if __name__ == "__main__":
    print("Running Tests for Smart Attendance System...\n")
    unittest.main(verbosity=2)
