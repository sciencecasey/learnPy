def computepay(h,r):
    h=float(h)
    r=float(r)
    if h<=40:
        pay=h*r
    elif h>40:
        base=40*r
        ot=1.5*r*(h-40)
        pay=base+ot
    return pay

hours=input("Enter this week's hours: ")
#h=float(hours)
rate=input("Enter hourly wage: ")
#r=float(rate)

p=computepay(hours,rate)
print(p)
