class BankAccount:
    """
    BankAccount Class
    
    This class represents a simple bank account with basic banking operations.
    It demonstrates object-oriented programming concepts including:
    - Constructor (__init__ method)
    - Instance variables (attributes)
    - Instance methods
    - Input validation
    - Error handling
    
    Attributes:
        name (str): The account holder's name
        balance (float): Current account balance
        account_number (str): Unique account identifier
        transaction_history (list): List of all transactions
    """
    
    def __init__(self, name, initial_balance=0.0):
        """
        Constructor method - called when creating a new BankAccount object
        
        Parameters:
            name (str): The account holder's name
            initial_balance (float): Starting balance (defaults to 0.0)
        
        This method initializes a new bank account with the given name and balance.
        It also generates a unique account number and initializes the transaction history.
        """
        # Validate input parameters
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Name must be a non-empty string")
        
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number")
        
        # Set instance variables (attributes)
        self.name = name.strip()  # Remove leading/trailing whitespace
        self.balance = float(initial_balance)  # Convert to float for precision
        
        # Generate a simple account number (in real applications, this would be more sophisticated)
        import random
        self.account_number = f"ACC{random.randint(10000, 99999)}"
        
        # Initialize transaction history list
        self.transaction_history = []
        
        # Add initial deposit to transaction history if balance > 0
        if initial_balance > 0:
            self.transaction_history.append({
                'type': 'Initial Deposit',
                'amount': initial_balance,
                'balance_before': 0.0,
                'balance_after': self.balance,
                'timestamp': self._get_timestamp()
            })
        
        print(f"✅ Bank account created successfully for {self.name}")
        print(f"   Account Number: {self.account_number}")
        print(f"   Initial Balance: ${self.balance:.2f}")
    
    def _get_timestamp(self):
        """
        Private method to get current timestamp
        
        Returns:
            str: Formatted current timestamp
        
        This is a helper method (denoted by the underscore prefix) that
        generates timestamps for transactions. It's not meant to be called
        directly by users of the class.
        """
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def deposit(self, amount):
        """
        Deposit method - adds money to the account
        
        Parameters:
            amount (float): Amount to deposit (must be positive)
        
        Returns:
            bool: True if deposit successful, False otherwise
        
        This method validates the deposit amount, adds it to the balance,
        records the transaction, and provides feedback to the user.
        """
        # Input validation
        if not isinstance(amount, (int, float)):
            print("❌ Error: Amount must be a number")
            return False
        
        if amount <= 0:
            print("❌ Error: Deposit amount must be positive")
            return False
        
        # Perform the deposit
        old_balance = self.balance
        self.balance += amount
        
        # Record the transaction
        transaction = {
            'type': 'Deposit',
            'amount': amount,
            'balance_before': old_balance,
            'balance_after': self.balance,
            'timestamp': self._get_timestamp()
        }
        self.transaction_history.append(transaction)
        
        # Provide user feedback
        print(f"✅ Deposit successful!")
        print(f"   Amount deposited: ${amount:.2f}")
        print(f"   Previous balance: ${old_balance:.2f}")
        print(f"   New balance: ${self.balance:.2f}")
        
        return True
    
    def withdraw(self, amount):
        """
        Withdraw method - removes money from the account
        
        Parameters:
            amount (float): Amount to withdraw (must be positive and <= balance)
        
        Returns:
            bool: True if withdrawal successful, False otherwise
        
        This method checks if there are sufficient funds, validates the amount,
        performs the withdrawal, records the transaction, and provides feedback.
        """
        # Input validation
        if not isinstance(amount, (int, float)):
            print("❌ Error: Amount must be a number")
            return False
        
        if amount <= 0:
            print("❌ Error: Withdrawal amount must be positive")
            return False
        
        # Check if sufficient funds are available
        if amount > self.balance:
            print("❌ Error: Insufficient funds!")
            print(f"   Requested: ${amount:.2f}")
            print(f"   Available: ${self.balance:.2f}")
            return False
        
        # Perform the withdrawal
        old_balance = self.balance
        self.balance -= amount
        
        # Record the transaction
        transaction = {
            'type': 'Withdrawal',
            'amount': amount,
            'balance_before': old_balance,
            'balance_after': self.balance,
            'timestamp': self._get_timestamp()
        }
        self.transaction_history.append(transaction)
        
        # Provide user feedback
        print(f"✅ Withdrawal successful!")
        print(f"   Amount withdrawn: ${amount:.2f}")
        print(f"   Previous balance: ${old_balance:.2f}")
        print(f"   New balance: ${self.balance:.2f}")
        
        return True
    
    def check_balance(self):
        """
        Check balance method - displays current account balance
        
        Returns:
            float: Current account balance
        
        This method displays the current balance and account information
        without modifying the account state.
        """
        print(f"\n💰 Account Balance for {self.name}")
        print(f"   Account Number: {self.account_number}")
        print(f"   Current Balance: ${self.balance:.2f}")
        return self.balance
    
    def get_transaction_history(self):
        """
        Get transaction history method - displays all account transactions
        
        Returns:
            list: List of all transactions
        
        This method shows a formatted list of all transactions including
        deposits, withdrawals, and their timestamps.
        """
        if not self.transaction_history:
            print("📋 No transactions found")
            return []
        
        print(f"\n📋 Transaction History for {self.name}")
        print(f"   Account Number: {self.account_number}")
        print("-" * 80)
        print(f"{'Type':<15} {'Amount':<12} {'Balance Before':<15} {'Balance After':<15} {'Timestamp':<20}")
        print("-" * 80)
        
        for transaction in self.transaction_history:
            print(f"{transaction['type']:<15} "
                  f"${transaction['amount']:<11.2f} "
                  f"${transaction['balance_before']:<14.2f} "
                  f"${transaction['balance_after']:<14.2f} "
                  f"{transaction['timestamp']:<20}")
        
        return self.transaction_history
    
    def __str__(self):
        """
        String representation method - called when printing the object
        
        Returns:
            str: Formatted string representation of the account
        
        This method provides a readable string representation of the
        BankAccount object when it's printed or converted to a string.
        """
        return f"BankAccount(name='{self.name}', balance=${self.balance:.2f}, account_number='{self.account_number}')"
    
    def __repr__(self):
        """
        Detailed string representation method - used for debugging
        
        Returns:
            str: Detailed string representation of the account
        
        This method provides a detailed representation useful for debugging
        and development purposes.
        """
        return f"BankAccount(name='{self.name}', balance={self.balance}, account_number='{self.account_number}')"


def demonstrate_bank_account():
    """
    Demonstration function to show how to use the BankAccount class
    
    This function creates a bank account and demonstrates various
    banking operations including deposits, withdrawals, and balance checks.
    """
    print("🏦 Bank Account System Demonstration")
    print("=" * 50)
    
    try:
        # Create a new bank account
        print("\n1. Creating a new bank account...")
        account = BankAccount("John Doe", 1000.00)
        
        # Demonstrate various operations
        print("\n2. Performing deposits...")
        account.deposit(500.00)
        account.deposit(250.50)
        
        print("\n3. Checking balance...")
        account.check_balance()
        
        print("\n4. Performing withdrawals...")
        account.withdraw(200.00)
        account.withdraw(1000.00)  # This should fail due to insufficient funds
        
        print("\n5. Final balance check...")
        account.check_balance()
        
        print("\n6. Transaction history...")
        account.get_transaction_history()
        
        # Demonstrate error handling
        print("\n7. Testing error handling...")
        account.deposit(-100)  # Invalid negative amount
        account.withdraw(0)    # Invalid zero amount
        account.deposit("abc") # Invalid non-numeric amount
        
    except Exception as e:
        print(f"❌ An error occurred: {e}")


def interactive_bank_demo():
    """
    Interactive demonstration function for user input
    
    This function allows users to interactively test the bank account
    functionality by entering their own values for deposits and withdrawals.
    """
    print("\n🎮 Interactive Bank Account Demo")
    print("=" * 40)
    
    try:
        # Get user input for account creation
        name = input("Enter account holder name: ").strip()
        if not name:
            name = "Demo User"
        
        initial_balance = input("Enter initial balance (or press Enter for $0): ").strip()
        if not initial_balance:
            initial_balance = 0.0
        else:
            initial_balance = float(initial_balance)
        
        # Create account
        account = BankAccount(name, initial_balance)
        
        while True:
            print("\n" + "="*40)
            print("Choose an operation:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. View Transaction History")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                account.check_balance()
                
            elif choice == '2':
                try:
                    amount = float(input("Enter deposit amount: $"))
                    account.deposit(amount)
                except ValueError:
                    print("❌ Invalid amount. Please enter a number.")
                    
            elif choice == '3':
                try:
                    amount = float(input("Enter withdrawal amount: $"))
                    account.withdraw(amount)
                except ValueError:
                    print("❌ Invalid amount. Please enter a number.")
                    
            elif choice == '4':
                account.get_transaction_history()
                
            elif choice == '5':
                print("👋 Thank you for using the Bank Account System!")
                break
                
            else:
                print("❌ Invalid choice. Please enter 1-5.")
                
    except KeyboardInterrupt:
        print("\n👋 Demo interrupted. Goodbye!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    """
    Main execution block
    
    When this script is run directly (not imported), it will:
    1. Run the demonstration function
    2. Start the interactive demo
    """
    # Run the demonstration
    demonstrate_bank_account()
    
    # Start interactive demo
    interactive_bank_demo()
