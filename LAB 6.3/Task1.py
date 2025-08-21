class Student:
    """
    A Student class with attributes and methods for managing student information.
    """
    
    def __init__(self, name, roll_no, marks):
        """
        Initialize a Student object with name, roll number, and marks.
        
        Args:
            name (str): Student's name
            roll_no (str): Student's roll number
            marks (float): Student's marks (0-100)
        """
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def display_details(self):
        """
        Display all student details in a formatted manner.
        """
        print("=" * 40)
        print("STUDENT DETAILS")
        print("=" * 40)
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")
        print("=" * 40)
    
    def calculate_grade(self):
        """
        Calculate grade based on marks according to the specified criteria.
        
        Returns:
            str: Grade (A, B, C, or Fail)
        """
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "Fail"


# Test the Student class
if __name__ == "__main__":
    # Create test students with different marks
    print("Testing Student Class\n")
    
    # Student 1: Grade A
    student1 = Student("Alice Johnson", "2024001", 95.5)
    student1.display_details()
    
    print()
    
    # Student 2: Grade B
    student2 = Student("Bob Smith", "2024002", 82.0)
    student2.display_details()
    
    print()
    
    # Student 3: Grade C
    student3 = Student("Carol Davis", "2024003", 68.5)
    student3.display_details()
    
    print()
    
    # Student 4: Fail
    student4 = Student("David Wilson", "2024004", 45.0)
    student4.display_details()
    
    print("\n" + "=" * 50)
    print("GRADE CRITERIA:")
    print("A: >= 90 marks")
    print("B: >= 75 marks")
    print("C: >= 60 marks")
    print("Fail: < 60 marks")
    print("=" * 50)
