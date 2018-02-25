
def help_menue():
    # this is the help variable
    help_men = """
    Python Calculator
    Select Mode:
        1 - Noraml Mode
        2 - EQN Mode
        3 - MATRIX
    """
    print(help_men)

help_menue() # call the menue function
h = raw_input("s> ") # get input from the user
print(h) # print value of h

# create endless while loop
while True:
    # use if to select one mode
    if h == '1':
        print("Normal Mode Activated: ")
    if h == '2':
        print("EQN Mode Activated: ")
    if h == '3':
        print("MATRIX Mode Activated: ")
