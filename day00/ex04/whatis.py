import sys

arg1 = sys.argv[1:]
if arg1 != []:
    arg2 = arg1[1:]
    if arg2 != []:
        print("AssertionError: more than one argument is provided")
    else:
        try:
            num = int(arg1[0])
            if num % 2:
                print("I'm Odd")
            else:
                print("I'm Even")
        except:
            print("AssertionError: argument is not an integer")
        
