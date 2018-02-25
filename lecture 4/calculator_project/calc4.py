
def help_menue():
    # this is the help variable
    help_men = """
    Python Calculator
    Select Mode:
        1 - Noraml Mode
        2 - EQN Mode
        3 - MATRIX
        x - Exit
    """
    print(help_men)

# create endless while loop
while True:
    help_menue() # call the menue function
    h = raw_input("s> ") # get input from the user
    print(h) # print value of h
    
    # use if to select one mode
    if h == '1':
        print("Normal Mode Activated: ")
    if h == '2':
        print("EQN Mode Activated: ")
    if h == '3':
        print("MATRIX Mode Activated: ")
    if h == 'x':
        break # exit from the program if h equal x
