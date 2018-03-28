s=raw_input("Enter a sentence :")
l=len(s)
dic=dict()
for i in range (0,l):
    if not dic.has_key(s[i]):
        dic[s[i]]=1
    else:
        dic[s[i]]=dic[s[i]]+1
print dic
