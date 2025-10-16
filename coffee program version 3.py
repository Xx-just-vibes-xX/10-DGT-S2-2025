# Creating an input system for our coffee program
# Timea Croucamp
# Date: 10/10/2025

# Version 2
# TODO: Ask the user if they like coffee
#       Record their answer
#       Give a response back to the user

# Version 1
# Ask the user whether they like coffee or not
'''like_coffee = input("Do you like coffee?")
print(f'Your answer was "{like_coffee}".')

if like_coffee == "yes" or "Yes" or "y" or "Y" :
    print("That is great! I like coffee too.")

else:
    print("You are missing out! Why not give it a try?")'''

# Version 2
# While loop
'''keep_going = "" # The variable contains an empty string
while keep_going == "":
    like_coffee = input("Do you like coffee?")

    if like_coffee == "yes" or like_coffee == "Yes" or like_coffee == "y" or like_coffee == "Y":
        print("That is great! I like coffee too.")
        keep_going ="finished"
        
    elif like_coffee == "No" or like_coffee == "no" or like_coffee == "N" or like_coffee ==  "n":
        print("You are missing out! Why not give it a try?")
        keep_going ="finished"
        

    else: 
        print("I dont understand.")'''

# Version 3
# Making program more pythonic
keep_going = ""
while keep_going == "":
    # Convert answer to lower case using .lower()
    like_coffee = input("Do you like coffee? \n") .lower()
    if like_coffee == "yes" or like_coffee == "y":
       print("That's great! I like coffee too!")

    elif like_coffee == "no":
        print("You are missing out! Why not give it a try?")

        like_tea = input("Do you like tea instead?") .upper()
        if like_tea == "YES" or like_tea == "Y":
            print("Good for you. Give coffee another try :)")

        elif like_tea == "NO" or like_tea == "N":
            print("I am sorry. That is all I have for now.")

        else:
            print("I don't understand. Please answer with either Yes or No")

else: # Error message 
    print("I don't understand. Please answer with either Yes or No")

keep_going = input("Press <ENTER> to continue, or any other key to quit. Thanks!")

    




