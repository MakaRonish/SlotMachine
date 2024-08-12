li=["1","2","3"]
li1=["1","2","1"]
c=0
for a,b in zip(li,li1):
    if a==b:
        c+=1
print(c)