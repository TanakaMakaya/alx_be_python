def display_current_datetime():
    """
    Displays the current date and time in a human-readable format.
    """
    from datetime import datetime
    now = datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

def display_datetime_info():
    """
    Displays various information about the current date and time.
    """
    from datetime import datetime
    now = datetime.now()
    
    print("Year:", now.year)
    print("Month:", now.month)
    print("Day:", now.day)
    print("Hour:", now.hour)
    print("Minute:", now.minute)
    print("Second:", now.second)
    print("Weekday (0=Monday):", now.weekday())
    print("ISO format:", now.isoformat())