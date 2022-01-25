import re
fname=input("Enter file name: ")
handle=open(fname)
sum=0
for line in handle :
    num=re.findall("[0-9]+",line)
    for i in num :
        sum=sum+int(i)
print(sum)
