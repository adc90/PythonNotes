#Hello

def reciprocal(a,b):
   if b == 0:
      raise ZeroDivisionError
   return a/b

try: 
    print reciprocal(1,0)
except ZeroDivisionError as e:
    print e
finally:
    print "This is always called"

