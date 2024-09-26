import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:-1]:#couting from the end of the list 
    print("Hello, my name is", arg)

#slice from the end
