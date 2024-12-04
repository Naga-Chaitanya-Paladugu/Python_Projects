# #Task
# The provided code stub reads two integers from STDIN,
# and . Add code to print three lines where:
#
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Example
# a= 3
# b= 5

# Print the following:
# 8
# -2
# 15


def arithmetic_operator(a: int, b: int) -> int:
    value = None
    # You do the algebra needed to figure out what c is
    # print(a + b)
    # print(a - b)
    # print(a * b)
    return value


if __name__ == '__main__':
    while True:
        try:
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
            print(f"Your answer is: {arithmetic_operator(a, b)}")
            break
        except:
            print('Enter valid integer input')
