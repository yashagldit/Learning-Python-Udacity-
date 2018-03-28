def area(a,b,c):
    if(a+b>c and b+c>a and a+c>b):
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print "Area of triangle = ",area
    else:
        print "Area Can't be calculated"

def main():
    a=int(input("Enter a :"))
    b=int(input("Enter b :"))
    c=int(input("Enter c :"))
    area(a,b,c)

if __name__== "__main__":
    main()

