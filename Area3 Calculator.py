import time

# I could have programed better but i was lazy, also nocopyright.

def calculateArea3(x,y,z):
   print("\n")
   print("Area3:",x*y*z,"\n")
   print("Circumference:",x+y+z,"\n")
   input("Press enter to exit program.")
def start_question():
    x = input("First Number: ")
    y = input("Second Number: ")
    z = input("Third Number: ")
    time.sleep(1)
    calculateArea3(int(x),int(y),int(z))

start_question()
