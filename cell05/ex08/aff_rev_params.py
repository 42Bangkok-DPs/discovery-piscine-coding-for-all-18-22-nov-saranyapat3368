import sys

if len(sys.argv) > 2:
    
    for param in reversed(sys.argv[1:]):
        print(param)
else:
    
    print('"none"')