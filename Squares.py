def my_func():

    import pyfiglet

    import math

    import time

    import random

    a=pyfiglet.figlet_format("Square")

    b=pyfiglet.figlet_format("root")

    c=pyfiglet.figlet_format("Generator")

    print(a,b,c)

    a=random.randint(1,10000)

    x=math.sqrt(a)

    print("The square root of ",a,"is",x,("\n"))

    print("_"*65,"\n")

    print("               Wait a seconds :")

    time.sleep(3)

    print("\n")

    

while 1<3 :

        

        my_func()     
