# Conversion calculator
# Author: Timea Croucamp
# Date: 11 / 11 / 2025

print("Welcome to the conversion calculator! :)")

name = input("Please enter your name: ")
print(f"Hello {name}!")

#mass=m distance=d time=t

keep_going = ""
while keep_going == "":
    typecalc = input("Please enter your type of calculation required - where mass = m, distance = d, time = t - or to exit the program, type 'quit': ")

    print("Please follow the instructions to successfully convert your given values to your desired units!")

    if typecalc == "quit":
        print("You have ended the program. Have a nice day!")
        print(f"Thank you for using the conversion calculator, {name}")
        break

    if typecalc == "d":

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

        distance_dict = {
            "mm": 1000,
            "cm": 100,
            "m": 1,
            "km": .001
        }

        # Get amount and units (assume they are valid)
        while True:
            amount = num_check(f"{name}, what is the number you are converting?: ")
            from_unit = input("From unit? Please only choose from km, m, cm, mm!: ").lower()
            to_unit = input("To unit? Please only choose from km, m, cm, mm!: ").lower()

            '''if from_unit not in distance_dict and to_unit not in distance_dict:
                print("You have entered an invalid unit. Please choose from km, m, cm, mm!")
            else:
                # Multiply to get our standard value...
                multiply_by = distance_dict[to_unit]
                standard = amount * multiply_by'''

            if to_unit not in distance_dict or from_unit not in distance_dict:
                print(f"You have entered an invalid unit. {name}, please choose from km, m, cm, mm!")
                
            else:
                # Multiply to get our standard value...
                multiply_by = distance_dict[to_unit]
                standard = amount * multiply_by
                # Divide to get our desired value
                divide_by = distance_dict[from_unit]
                answer = standard / divide_by

                print(f"{amount} {from_unit} is equal to {answer} {to_unit}")
                break # exit the unit loop once it is successful


    elif typecalc == "m":

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

        mass_dict = {
            "mg": 1000000,
            "g": 1000,
            "kg": 1,
            "t": .001
        }

        # Get amount and units (assume they are valid)
        while True:
            amount = num_check(f"{name}, what is the mass number you are wanting to convert?: ")
            from_unit = input("From mass unit? Please only choose from mg, g, kg, t ;) : ").lower ()
            to_unit = input("To mass unit? Again, please only choose from mg, g, kg, t ;D : ").lower ()

            if to_unit not in mass_dict or from_unit not in mass_dict:
                print("You have entered an invalid unit. Please choose from mg, g, kg, t!")
                
            else:
                # Multiply to get our standard value...
                multiply_by = mass_dict[to_unit]
                standard = amount * multiply_by
                # Divide to get our desired value
                divide_by = mass_dict[from_unit]
                answer = standard / divide_by

                print(f"{amount} {from_unit} is equal to {answer} {to_unit}")
                break # exit the mass unit loop after successful


    elif typecalc == "t":

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

        time_dict = {
            "ms": 1000,
            "sec": 1,
            "min": 1/60,
            "hrs": 1/3600,
            "days": 1/86400,
            "weeks": 1/604800, 
            "years": 1/31557600
        }

        # Get amount and units (assume they are valid)
        while True:
            amount = num_check(f"{name}, what is the time conversion you want to do?: ")
            from_unit = input("From time unit? Please only choose from ms, sec, min, hrs, days, weeks, years :) : ").lower ()
            to_unit = input("To time unit? Again, please only choose from ms, sec, min, hrs, days, weeks, years :) : ").lower ()

            if to_unit not in time_dict or from_unit not in time_dict:
                print("You have entered an invalid unit. Please only choose from ms, sec, min, hrs, days, weeks, years!")
                
            else:
                # Multiply to get our standard value...
                multiply_by = time_dict[to_unit]
                standard = amount * multiply_by
                # Divide to get our desired value
                divide_by = time_dict[from_unit]
                answer = standard / divide_by

                print(f"{amount} {from_unit} is equal to {answer} {to_unit}")
                break # exit the time conversion loop once successful
    else:
        print(f"{name}, you have entered an invalid selection.*")
