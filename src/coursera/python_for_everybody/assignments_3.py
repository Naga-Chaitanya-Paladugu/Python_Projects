# Write a program to prompt the user for hours and rate per hour using input to
# compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate
# for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to
# test the program (the pay should be 498.75). You should use input to read a string and
# float() to convert the string to a number.


def monthly_pay(hours: float, rate: float):
    # hrs = input("Enter Hours:")
    # h = float(hrs)
    #rate = float(input('Enter hourly rate:'))
    if hours <= float(40):
        rate = rate
    else:
        rate = 1.5 * rate
    gross_pay = hours * rate
    print(gross_pay)

if __name__ == '__main__':
    monthly_pay(45, 10.75)