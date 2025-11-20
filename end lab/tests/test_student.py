import unittest

from task1 import Student


class TestStudentAttendance(unittest.TestCase):

    def test_initial_values(self):
        student = Student("Ayesha", "22CSE31")
        self.assertEqual(student.total_classes, 0)
        self.assertEqual(student.attended_classes, 0)
        self.assertEqual(student.attendance_percentage(), 0.0)

    def test_mark_attendance_present(self):
        student = Student("Ayesha", "22CSE31")
        student.mark_attendance(True)
        self.assertEqual(student.total_classes, 1)
        self.assertEqual(student.attended_classes, 1)
        self.assertEqual(student.attendance_percentage(), 100.0)

    def test_mark_attendance_absent(self):
        student = Student("Ayesha", "22CSE31")
        student.mark_attendance(False)
        self.assertEqual(student.attended_classes, 0)
        self.assertEqual(student.attendance_percentage(), 0.0)

    def test_calculate_percentage(self):
        student = Student("Ayesha", "22CSE31")
        student.mark_attendance(True)
        student.mark_attendance(True)
        student.mark_attendance(False)
        self.assertEqual(student.attendance_percentage(), 66.67)


if __name__ == "__main__":
    unittest.main()
