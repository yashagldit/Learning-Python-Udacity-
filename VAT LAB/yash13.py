n=input("Enter size : ")
for i in range(1,n):
    for j in range(1,n-i):
        print ' ',
    for k in range(1,i):
        print k,
    for l in range(i,0,-1):
        print l,
    print ''
