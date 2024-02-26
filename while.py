# Continually getting number as a user input and output the average of the numbers input

total = 0 # Creating variable to store sum of the entered numbers

user_input_count = 0 # Creating variable to store count of the entered numbers

# Getting number as a user input and casting it into a integer

user_input = int(input("Please enter a number or enter -1 to exit: "))

# Creating while loop to iterate user input requesting
# If user_input not equal to -1, then loop is activating

while user_input != -1: 

    # Store sum of the user inputs into "total"
    total += user_input  
    
    # Count every user inputs without -1
    user_input_count += 1 

    # Request user input after every iteration
    user_input = int(input("Please enter a number or enter -1 to exit: ")) 

    # Creating nested if statement to calculate and display Average of the entered numbers
    if user_input == -1:
        print(f"You have successfully exited.\nAverage of the numbers you entered: {total/user_input_count}")
        break