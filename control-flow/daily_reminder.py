task = input("input a task description: ")
priority = input("task's priority (high/medium/low): ").lower()
time_bound = input("task is time-bound (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task}. is a high priority task that requires immediate attention today!")
        else:
            print(f"High priority task: {task}. Make sure to complete it today.")
    case "medium":
        if time_bound == "yes":
            print(f"Medium priority task: {task}. Try to finish it within the next few days.")
        else:
            print(f"Medium priority task: {task}. You can complete it this week.")
    case "low":
        if time_bound == "yes":
            print(f"Low priority task: {task}. You can take your time, but try to finish it soon.")
        else:
            print(f"Low priority task: {task}. No rush, you can do it whenever you have time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")