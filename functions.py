def f1():
    print "9 * 6"

def f2():
    print 42

def f3a(argu):
    print argu
    print type (argu)
    argu = "the answer"

print f1()
print f2()
print f3a(argu)