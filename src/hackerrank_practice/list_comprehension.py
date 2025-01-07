def list_maker(coordinates: int):
    lst = []
    for i in range(0, coordinates + 1):
        lst.append(i)
    return lst


def coordinates_permutation(list1: list, list2: list, list3: list):
    tmp_lst = []
    return [[i, j, k] for i in list1 for j in list2 for k in list3 if i + j + k != n]
    # for i in x_list:
    #     for j in y_list:
    #         for k in z_list:
    #             if i+j+k==n:
    #                 continue
    #             tmp_lst.append([i, j, k])
    # return tmp_lst


if __name__ == '__main__':
    x = int(input('Enter number: '))
    y = int(input('Enter number: '))
    z = int(input('Enter number: '))
    n = int(input('Enter comparison number: '))
    x_list = list_maker(x)
    y_list = list_maker(y)
    z_list = list_maker(z)
    print(coordinates_permutation(x_list, y_list, z_list))
