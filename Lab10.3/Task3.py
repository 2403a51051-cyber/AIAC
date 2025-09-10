class Employee:
    """
    Represents an employee with a name and salary.
    """

    def __init__(self, name, salary):
        """
        Initialize an Employee instance.

        Args:
            name (str): The employee's name.
            salary (float): The employee's salary.
        """
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        """
        Increase the employee's salary by a given percentage.

        Args:
            percent (float): The percentage to increase the salary.
        """
        self.salary += self.salary * percent / 100

    def display_info(self):
        """
        Display the employee's information in a formatted way.
        """
        print(f"Employee Name: {self.name}")
        print(f"Current Salary: ${self.salary:,.2f}")

if __name__ == "__main__":
    name = input("Enter employee name: ")
    try:
        salary = float(input("Enter employee salary: "))
        percent = float(input("Enter salary increment percentage: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for salary and percentage.")
    else:
        emp = Employee(name, salary)
        emp.increase_salary(percent)
        emp.display_info()    