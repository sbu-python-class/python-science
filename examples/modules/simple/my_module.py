
print "this statement executes upon import"

def fun_A():
    """ print some text """
    print "in fun_A"

def fun_B():
    """ print some different text """
    print "in fun_B"

if __name__ == "__main__":
    import sys
    print "arguments: ", sys.argv[1:]

    fun_A()
    fun_B()


        
