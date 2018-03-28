arr=list()
flag=0
i=0
while(i<5):
    while(flag==0):
        x=raw_input(i)
        if(len(x)>6):
            flag=1
            print x
            break
        elif(len(x)<6):
            print "Enter again"
        else:
            arr.append(x)
            i=i+1
print arr

