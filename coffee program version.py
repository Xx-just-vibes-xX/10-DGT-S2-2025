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
keep_going = "" # The variable contains an empty string
while keep_going == "":
    like_coffee = input("Do you like coffee?")

    if like_coffee == "yes" or like_coffee == "Yes" or like_coffee == "y" or like_coffee == "Y":
        print("That is great! I like coffee too.")
        keep_going ="finished"
        
    elif like_coffee == "No" or like_coffee == "no" or like_coffee == "N" or like_coffee ==  "n":
        print("You are missing out! Why not give it a try?")
        keep_going ="finished"
        

    else: 
        print("I dont understand.") 




