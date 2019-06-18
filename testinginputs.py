#program testing arithmetic functions for pay with inputs

hrs=input("Enter hours worked per day: ")
pay=input("Enter the hourly wage: ")
days=input("Enter days worked per week: ")
weeks=input("Weeks to calculate: ")
gross=float(hrs)*float(days)*float(weeks)*float(pay)
print("Gross pay", gross)
