# 5.2 Write a program that repeatedly prompts a user for
# integer numbers until the user enters 'done'. Once 'done' is entered,
# print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with
# a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

if __name__ == '__main__':
    largest = None
    smallest = None
    while True:
        num = input('Enter a number: ').lower()
        if num == 'done':
            break
        else:
            try:
                num_float = float(num)
            except:
                print('Please enter a valid input number')
                continue
            if largest is None:
                largest = num_float
                smallest = num_float
                continue
            elif num_float > largest:
                largest = num_float
            elif num_float < smallest:
                smallest = num_float
    if largest is None or smallest is None:
        print('No number entered till now! So by default it is None')
    else:
        print(f'The largest number is {largest}, {smallest}')
