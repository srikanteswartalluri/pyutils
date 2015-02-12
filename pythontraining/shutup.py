__author__ = 'talluri'
while True:
    string = raw_input("Enter message:")
    string.rstrip()
    if string == "ShutUp":
        break
    else:
        print "%s" % string[::-1]
