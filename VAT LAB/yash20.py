n=int(input("Enter no. of rows"))
for i in range (0,n):
    for j in range(n,i,-1):
        print "  ",
    for j in range(i+1,0,-1):
        print j,"",
    for j in range(2,i+2):
        print j,"",
    print ''
