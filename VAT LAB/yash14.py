n=input("Enter size : ")
for i in range(1,n+1):
    for j in range(1,i+1):
        print '*',
    print ''
for i in range(1,n):
    for j in range(n,i,-1):
        print '*',
    print ''
