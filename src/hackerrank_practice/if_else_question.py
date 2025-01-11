if __name__ == '__main__':
    for n in range(-1, 102):
        result = None
        if n< 1 or n> 100:
            continue
        if n % 2 == 1:
            result = 'Weird'
        elif n % 2 == 0:
            if n in [2, 3, 4, 5]:
                result = 'Not Weird'
            elif 6 <= n <= 20:
                result = 'Weird'
            else:
                result = 'Not Weird'


        print(f"{result}")

##### learnings:
#1. range(start, stop, step). not just range(5).

# 2. Situations Where None is Used:
# Functions without a return statement or with return alone automatically return None.
# Used to indicate "no result" or invalid outcomes in conditions.
# Used as an initial value for variables that will be assigned later.
#
# def find_item(items, target):
#     if target not in items:
#         return None
#
# result = None
