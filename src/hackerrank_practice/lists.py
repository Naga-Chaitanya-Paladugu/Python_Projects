def list_builder():
    for _ in range(n):
        command = input('Enter the command: ').split()
        if command[0] == 'insert':
            method_name = command[0]
            index, value = int(command[1]), int(command[2])
            getattr(lst, method_name)(index, value)
        elif len(command)>1:
            method_name = command[0]
            argument= int(command[1])
            getattr(lst, method_name)(argument)
        elif command[0] == 'print':
            print(lst)
        else:
            method_name = command[0]
            getattr(lst, method_name)()

if __name__ == '__main__':
    lst = list()
    n = int(input('Total number of entries: '))
    list_builder()




########learnings:
# 0. Dynamic method execution
# lst.append(argument) is a direct, simple call.
# getattr(lst, method_name)(argument) provides flexibility for dynamic method execution.

# 1. insert i e:
#
# Inserts integer e at position i.
# Note: Shifts elements to the right, if index given out of range inserts it at end just like append.
# my_list = [1, 2, 4]
# my_list.insert(2, 3)  # Insert 3 at index 2
# print(my_list)  # Output: [1, 2, 3, 4]

# 2. remove e:

# Deletes the first occurrence of integer e.
# Note: Raises a ValueError if e is not in the list.
# my_list = [1, 2, 3, 2]
# my_list.remove(2)  # Remove first occurrence of 2
# print(my_list)  # Output: [1, 3, 2]

# 3. append e:
#
# Adds integer e to the end of the list.
# Note: Equivalent to insert(len(list), e).
# my_list = [1, 2, 3]
# my_list.append(4)  # Append 4 at the end
# print(my_list)  # Output: [1, 2, 3, 4]

# 4. pop:
#
# Removes and returns the last element of the list.
# Note: Raises an IndexError if the list is empty.
# my_list = [1, 2, 3]
# last = my_list.pop()  # Pop the last element
# print(last)  # Output: 3
# print(my_list)  # Output: [1, 2]

# 5. reverse:
#
# Reverses the list in place.
# Note: Does not create a new list, modifies the original.
# my_list = [1, 2, 3]
# my_list.reverse()  # Reverse the list
# print(my_list)  # Output: [3, 2, 1]
