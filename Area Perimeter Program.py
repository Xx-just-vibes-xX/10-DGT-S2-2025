# Area Perimeter
# Author: Timea Croucamp
# Date: 29 / 10 / 2025
# Version 1   

# Ask user for width and loop until they
# enter a number that is more than zero

def num_check(question):...

# Main Routine starts here...

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check ("Width: ")
    height = num_check("Height: ")

    # Calculate area / perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print()
    print(f"Perimeter : {perimeter} units")
    print(f"Area: {area} square units")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator")
