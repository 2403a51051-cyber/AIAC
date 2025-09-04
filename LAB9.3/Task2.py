# Define the sru_student class
class sru_student:
    # Initialize the student object with name, roll number, and hostel status
    def __init__(self, name, roll_no, hostel_status):
        self.name = name              # Store the student's name
        self.roll_no = roll_no        # Store the student's roll number
        self.hostel_status = hostel_status  # Store hostel status (True/False)
        self.fee_paid = False         # Track if the fee has been paid

    # Method to update the fee status
    def fee_update(self, status):
        self.fee_paid = status        # Update the fee_paid attribute

    # Method to display student details
    def display_details(self):
        print("Name:", self.name)                     # Print the student's name
        print("Roll No.:", self.roll_no)              # Print the student's roll number
        print("Hostel Status:", self.hostel_status)   # Print hostel status
        print("Fee Paid:", self.fee_paid)             # Print fee payment status

# Example usage
student1 = sru_student("Alice", 101, True)    # Create a student object
student1.fee_update(True)                     # Update fee status to paid
student1.display_details()                    # Display student details
# ...existing code...
student1 = sru_student("Alice", 101, True)  # Create a new sru_student object
student1.fee_update(True)                   # Set the fee status to paid
student1.display_details()                  # Display all details of the student
# ...existing code...