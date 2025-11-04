# Author: Timea Croucamp
# Date: 4 / 11/ 2025
# Ask user for width and loop until they
# enter a number that is more than zero

print("Welcome to the area / perimeter calculator")

name = input("Please enter your name: ")
print(f"Hello {name}!")

print("Please follow the instructions for a successful outcome")

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

# Main routine starts here...

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area / perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator")
print("Have a wonderful day!")