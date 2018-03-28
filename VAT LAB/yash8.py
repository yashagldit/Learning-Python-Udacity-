num=input("Enter a no :")
tot=0
prime=0
while(num!=-1):
    tot=tot+1
    flag=0
    for i in range(2,num):
       if (num % i) == 0:
           flag=1
           break
    if(flag==0):
        prime=prime+1
    num=input("Enter a no.")
print "Prime no ",prime
print "Composite no. ",(tot-prime)
