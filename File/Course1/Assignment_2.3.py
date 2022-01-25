#hour=input('Enter hours: ')
#rate=input('Enter rate: ')
#pay=float(hour)*float(rate)
#print('Pay:', pay)

hour=input('Enter hours: ')
rate=input('Enter rate: ')
h=float(hour)
r=float(rate)
if h>40 :
    reg= r*h
    otp=(h-40.0) * (r*0.5)
    p=reg+otp
else :
   p=h*r
print(p)
