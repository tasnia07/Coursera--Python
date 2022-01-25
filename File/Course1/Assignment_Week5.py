#astr = 'Hello Bob'
#istr = 0
#try:
    #istr = int(astr)
#except:
    #istr = -1
#print(istr)

score=input("Enter Score: ")
try:
    s=float(score)
except:
    print("ERROR")
if s>=0.9 :
    print("A")
elif s>= 0.8 :
    print("B")
elif s>= 0.7 :
    print("C")
elif s>= 0.6 :
    print("D")
else:
    print("F")
