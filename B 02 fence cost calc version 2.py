# Calculate Fence Cost
# Author: Timea Croucamp
# Date: 7 / 11 / 2025

# Display the ValueError by creating an error message
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:
    
    # Create a try and except to manage the ValueError
        try:

            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        # Print the error message when the user has entered an invalid digit
        except ValueError:
            print(error)

# Main Routine of the program starts here...

# Greet the user and tell them what the program is
print("Welcome to the fence cost calculator :)")

# Ask the user for their name and greet them by their name
name = input("Please enter your name: ")
print(f"Hello {name}!")

# Tell the user to follow the given instructions to recieve the output
print("Please follow the instructions to find the fence cost of your given values!")

# Create a loop so that the user has the choice to keep going or stop
keep_going = ""
while keep_going == "":
    # Get the width and the height to calculate fence cost
    width = num_check (f"{name}, please enter your width (in metres): ")
    length = num_check("What is your length (in metres)?: ")
    # Ask the user for the cost to find the price for the fence cost
    cost = num_check("Please add your cost: ")

    # Calculate the perimeter and the price for the fence cost
    perimeter = 2 * (width + length)
    price = perimeter * cost

    # Display the output of the user's chosen numbers and display the perimeter 
    # units and the price of the fence cost
    print()
    print(f"The perimeter of your given values is: {perimeter} units")
    print(f"The price is: ${price:.2f}")

    # Ask user if they want to keep going or if they want to quit the program
    keep_going = input("Please press enter if you want to keep going or press any key to quit using the program. ")
    print()

# Greet the user goodbye when they press any other key to quit
print("Thank you for using the fence cost calculator.")
print("Have a wonderful day! I hope to see you again soon.")