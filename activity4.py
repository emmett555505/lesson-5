a = int(input("enter a value :"))
b = int(input("enter value 2 :"))
c = int(input("enter value 3 :"))

avg = (a +b +c) /3
print("the average =", avg)

if avg > a and avg > b and avg > c:
    print ("%d is higher that %d %d %d" %(avg, a, b, c))
elif avg > a and avg > b:
    print("%d is higher that %d %d" %(avg, a, b))
elif avg > a and avg > c:
    print("%d is higher that %d %d" %(avg, a, c))
elif avg > b and avg > c:
    print("%d is higher that %d %d" %(avg, b, c))
elif avg > a:
    print("%d is higher that %d " %(avg, a))
elif avg > b:
    print("%d is higher that %d " %(avg, b))
elif avg > c:
    print("%d is higher that %d " %(avg, c))
else:
    print("invalid input")
