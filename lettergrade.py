score = input("Enter Score: ")
s=float(score)

if s<.6:
    print('F')
elif s>=.6 and s<.7:
    print('D')
elif s>=.7 and s<.8:
    print('C')
elif s>=.8 and s<.9:
    print('B')
elif s>=.9 and s<=1:
    print('A')
else:
    print('input invalid')
