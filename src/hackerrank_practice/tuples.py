
if __name__ == '__main__':
    n= int(input())
    tup_elements= input().split()
    if len(tup_elements)==n:
            hashed_tup= hash(tuple(tup_elements))
            print(hashed_tup)
    else:
        print(f'please enter only {n} elements for the tuple')


##### learnings:

# 1. Key Points on hash():
# Purpose:
#
# Generates a unique integer for immutable objects (tuple, str, int).
# Used in hash-based structures (dict, set) for fast lookups.
#
# Restrictions:
#
# Only immutable objects are hashable (list and dict are not).
#
# Determinism:
#
# Hash values are consistent during a single program execution but may vary across runs for security.
#
# # Hashing a tuple
# t = (1, 2, 3)
# print(hash(t))  # Outputs a unique hash value for the tuple: -2064550735244679747
#
# # Using a tuple as a dictionary key
# my_dict = {t: "value"}
# print(my_dict)  # Output: {(1, 2, 3): 'value'}
#
# # Attempting to hash a mutable object (will raise an error)
# # print(hash([1, 2, 3]))  # TypeError: unhashable type: 'list'
