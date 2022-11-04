#Calculator
from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()
print( Back.GREEN )
print( Fore.BLACK )
print( Style.DIM)
what=input("What process will take place? (+,-,*,/): ")
a=float(input("Enter the firts number: "))
b=float(input("Enter the second mumber: "))
if what == "+":
    c=a+b
    print("Result: " +str(c))
elif what == "-":
    c=a-b
    print("Result: " +str(c))
elif what == "*":
    c=a*b
    print("Result: " +str(c))
elif what == "/":
    c=a/b
    print("Result: " +str(c))
else:
    print("Invalid operation selected!!!")
input()    
    
    
