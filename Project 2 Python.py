# Program to calculate future age

# Input: Get the current age of the user
current_age = input("Enter your current age: ")

# Validate input: Ensure it is a positive integer
if not current_age.isdigit() or int(current_age) < 0:
    print("Please enter a valid positive number for your age.")
else:
    current_age = int(current_age)
    
    # Input: Get the number of years to add
    years_to_add = input("Enter the number of years into the future: ")

    # Validate input: Ensure it is a positive integer
    if not years_to_add.isdigit() or int(years_to_add) < 0:
        print("Please enter a valid positive number for the years.")
    else:
        years_to_add = int(years_to_add)
        
        # Calculate the future age
        future_age = current_age + years_to_add
        
        # Output the result
        print(f"In {years_to_add} years, you will be {future_age} years old.")
