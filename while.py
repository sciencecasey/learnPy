#Write a program that repeatedly prompts a user for integer
#numbers until the user enters 'done'. Once 'done' is entered,
#print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number
#catch it with a try/except and
#put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.

x=None
while True:
    i=input('Type an integer: ')
    if i=='done':
        break
    try:
        n=int(i)
        if x is None:
            x=n
            smalls=x
            largs=x
        if smalls >= n:
            smalls = n
        if largs<=n:
            largs=n
    except:
        print('invalid entry')
        continue

print('The smallest is', smalls)
print('The largest is', largs)
