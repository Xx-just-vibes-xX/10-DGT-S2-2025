# Calculate Fence Cost
# Author: Timea Croucamp
# Date: 7 / 11 / 2025

print("Welcome to the fence cost calculator :)")

name = input("Please enter your name: ")
print(f"Hello {name}!")

print("Please follow the instructions to find the fence cost of your given values!")

def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:

            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine starts here...

keep_going = ""
while keep_going == "":
    # Get width and height
    width = num_check (f"{name}, please enter your width (in metres): ")
    length = num_check("What is your length (in metres)?: ")
    cost = num_check("Please add your cost: ")

    # Calculate perimeter and price for the fence
    perimeter = 2 * (width + length)
    price = perimeter * cost

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Price: ${price:.2f}")

    # Ask user if they want to keep going
    keep_going = input("Please press enter if you want to keep going or press any key to quit using the program. ")
    print()

print("Thank you for using the fence cost calculator.")
print("Have a wonderful day! I hope to see you again soon.")