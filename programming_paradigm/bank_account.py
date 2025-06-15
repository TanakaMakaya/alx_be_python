account = None

def load_or_create_account(initial_balance=0):
    """
    Create a new bank account or load existing one.
    
    Args:
        initial_balance (float): Initial balance for new accounts
    
    Returns:
        BankAccount: The account instance
    """
    global account
    if account is None:
        account = BankAccount(initial_balance)
        print(f"Created new bank account with initial balance: ${initial_balance:.2f}")
    return account

def handle_create_command(args):
    """Handle the 'create' command to create a new account."""
    try:
        initial_balance = float(args[2]) if len(args) > 2 else 0
        if initial_balance < 0:
            print("Error: Initial balance cannot be negative!")
            return
        
        global account
        account = BankAccount(initial_balance)
        print(f"✅ New bank account created!")
        account.display_balance()
        
    except ValueError:
        print("Error: Invalid initial balance. Please enter a valid number.")
    except IndexError:
        # No initial balance provided, use default
        account = BankAccount()
        print("✅ New bank account created with $0.00 balance!")

def handle_deposit_command(args):
    """Handle the 'deposit' command."""
    if len(args) < 3:
        print("Error: Please specify deposit amount.")
        print("Usage: python main-0.py deposit <amount>")
        return
    
    try:
        amount = float(args[2])
        acc = load_or_create_account()
        if acc.deposit(amount):
            acc.display_balance()
    except ValueError:
        print("Error: Invalid deposit amount. Please enter a valid number.")

def handle_withdraw_command(args):
    """Handle the 'withdraw' command."""
    if len(args) < 3:
        print("Error: Please specify withdrawal amount.")
        print("Usage: python main-0.py withdraw <amount>")
        return
    
    try:
        amount = float(args[2])
        acc = load_or_create_account()
        if acc.withdraw(amount):
            acc.display_balance()
    except ValueError:
        print("Error: Invalid withdrawal amount. Please enter a valid number.")

def handle_balance_command():
    """Handle the 'balance' command."""
    acc = load_or_create_account()
    acc.display_balance()
