def convert():
    hr=input("Enter Hour :")
    mn=input("Enter Min :")
    sc=input("Enter Sec :")
    s=sc%60
    a=sc/60
    mn=mn+a
    m=mn%60
    b=mn/60
    hr=hr+b
    print hr,m,s
convert()
