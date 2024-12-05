# 5.2 Write a program that repeatedly prompts a user for
# integer numbers until the user enters 'done'. Once 'done' is entered,
# print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with
# a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

if __name__=='__main__':
    largest= None
    while True:
        num= int(input('Enter a number: '))
        if num== done:
            break
        elif largest is None or num>largest:
            largest=num
    print('The largest number is',largest)