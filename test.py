#Hello

def reciprocal(a,b):
    if isinstance(a,str) or isinstance(b,str) == True:
        raise ValueError
    elif b == 0:
        raise ZeroDivisionError
    print a/b


try: 
    reciprocal('a','b')
except ZeroDivisionError as e:
    print "Zero Division Error has been caught"
except ValueError:
    print "Value Error has been caught"
finally:
    print "Enter a non-zero term for b"

