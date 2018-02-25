
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

def noraml_mode():
    # use while endless loop
    while True:
        exp = raw_input('Expression: ') # get exp input
        if exp == 'x':
            break # use break to end the loop
        print("out = "+ str( eval(exp) ) ) # use eval to evaluate math expression

# create endless while loop
while True:
    help_menue() # call the menue function
    h = raw_input("s> ") # get input from the user
    # print(h) print value of h
    
    # use if to select one mode
    if h == '1':
        print("Normal Mode Activated use (x) to exit: ")
        noraml_mode() # call the function
    if h == '2':
        print("EQN Mode Activated: ")
    if h == '3':
        print("MATRIX Mode Activated: ")
    if h == 'x':
        exit(0) # exit from the program if h equal x
