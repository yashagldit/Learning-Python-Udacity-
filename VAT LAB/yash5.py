import math
print "For ax^2+bx+c"
a=input("Enter a :")
b=int(input("Enter b :"))
c=input("Enter c :")
r1=((-b+math.sqrt((b*b-4*a*c)))/2*a)
r2=((-b-math.sqrt((b*b-4*a*c)))/2*a)
print "Roots are ",r1,r2
