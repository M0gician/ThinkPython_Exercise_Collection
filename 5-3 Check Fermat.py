def check_fermat(a, b, c, n):
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    
    if n < 3:
        print "No, that doesn't work."
    else:
        if a**n + b**n == c**n:
            print "Holy smokes, Fermat was wrong!"
        else:
            print "No, that doesn't work."

a = raw_input("a: ")
b = raw_input("b: ")
c = raw_input("c: ")
n = raw_input("n: ")

check_fermat(a, b, c, n)
