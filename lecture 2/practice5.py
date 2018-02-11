'''
from Celsius to Fahrenheit
F = C * (9 / 5) + 32
from Fahrenheit to Celsius
C = (F - 32) * (5 / 9)
'''
# take C as an iput
C = raw_input("Celsius :")
C = int(C)
# print(C)

# from Celsius to Fahrenheit
F = C * (9.0/5.0) + 32
print("Fahrenheit: "+str(F))

# from Fahrenheit to Celsius
F = raw_input("Fahrenheit: ")
F = float(F)
C = (F - 32) * (5.0 / 9.0)
print("Celsius :"+str(C))
