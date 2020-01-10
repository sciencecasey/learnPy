#coursera Python for Everyone
hrs = input("Enter Hours:")
rate=input("Enter Hourly wage:")
try:
    h = float(hrs)
    r=float(rate)
except:
    print('please use numerical input')
if h<=40:
    pay=h*r
    print(pay)
elif h>40:
    base=40*r
    ot=(h-40)*(1.5*r)
    pay=base+ot
    print(pay)
