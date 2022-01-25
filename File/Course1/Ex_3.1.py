#x=5
#if x > 2 :
    #print('Bigger than 2')
    #print('Still Bigger')
#print('Done with 2')

#for i in range(5) :
    #print(i)
    #if i>2 :
        #print('Bigger than 2')
    #print('Done with i:',i)
#print('All Done')
#a='Hello Bob'
#try :
    #i=int(a)
#except :
    #i=-1
#print('First',i)
#a='123'
#try :
    #i=int(a)
#except :
    #i=-1
#print('Second',i)

#def stuff():
    #print('Hello')
    #return
    #print('World')

#def addtwo(a, b):
    #added = a + b
    #x = addtwo(2, 7)
#print(x)

def computepay(h,r):
    if h>40 :
        reg= r*h
        otp=(h-40.0) * (r*0.5)
        ps=reg+otp
    else :
       ps=h*r
    return ps

hrs = input("Enter Hours: ")
rate=input("Enter Rate: ")
fh=float(hrs)
fr=float(rate)
p = computepay(fh,fr)
print("Pay",p)
