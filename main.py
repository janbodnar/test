
from datetime import datetime, date

def calculate_age(date_of_birth):
    """
    Calculate age from date of birth string.
    
    Args:
        date_of_birth (str): Date of birth in MM/DD/YYYY format
        
    Returns:
        int: Age in years
    """
    # Parse the date string (MM/DD/YYYY format)
    birth_date = datetime.strptime(date_of_birth, "%m/%d/%Y").date()
    
    # Get current date
    today = date.today()
    
    # Check if birth date is in the future
    if birth_date > today:
        return 0  # Return 0 for future dates
    
    # Calculate age
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    return age

print("hello there")

date_of_birth = "01/01/1970"

# Calculate and display age
age = calculate_age(date_of_birth)
print(f"Date of birth: {date_of_birth}")
print(f"Age: {age} years")