st=raw_input("Enter a string :")
def upper(st1):
    c=0
    for i in range(0,len(st1)):
        if(ord(st1[i])>=97 and ord(st1[i])<=122):
            c=c+1
    print "Lower ",c
def lower(st1):
    c=0
    for i in range(0,len(st1)):
        if(ord(st1[i])>=65 and ord(st1[i])<=91):
            c=c+1
    print "Upper ",c

def digit(st1):
    c=0
    for i in st1:
        for j in range(0,10):
            if(i==str(j)):
                c=c+1;
    print "Digit ",c

upper(st)
lower(st)
digit(st)
