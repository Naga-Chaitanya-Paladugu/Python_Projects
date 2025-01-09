# Task
# The provided code stub reads and integer, , from STDIN.
# For all non-negative integers , print .
#
# Example
# n= 3
# The list of non-negative integers that are less than n= 3 is [0, 1, 2].
# Print the square of each number on a separate line.
# 0
# 1
# 4

if __name__ == '__main__':
    n = int(input('Enter the number: '))
    i= 0
    while i<n:
        print(i*i)
        i+=1
    #     list.append(n)
    # for i in list:
    #     print(i ** 2)

# if __name__ == '__main__':
#     n = int(input('Enter the number: '))
#     list = []
#     while n > 0:
#         n = n - 1
#         list.append(n)
#     for i in list:
#         print(i * i)
