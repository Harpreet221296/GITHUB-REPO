#calculation of fine
def fine_calculator(days_overdue):
    # Check for negative input
    while days_overdue < 0:
        print("Please enter a non-negative number of days.")
        days_overdue = int(input("Enter the number of days that the book is overdue: "))

    # Calculate the fine
    fine = 1.00 + (days_overdue - 1) * 0.50
    return fine

# Get user input for the number of days the book is overdue
days_overdue = int(input("Enter the number of days that the book is overdue: "))

# Calculate and print the fine
fine = fine_calculator(days_overdue)
print(f"The fine for {days_overdue} days overdue is ${fine:.2f}.")