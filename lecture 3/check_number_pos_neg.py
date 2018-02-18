x = raw_input(" Number : ") # get the input from the user 
x = int(x)# transfer number to int
if x > 0:
    print("posative")
    
    if x % 2 == 0 :
        print("even")
    else:
        print("odd")
        
elif x == 0:
    print("Zero")
else:
    print("negative")


