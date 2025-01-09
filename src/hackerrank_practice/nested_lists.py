def runner_up():
    print(student_list)

    #creating unique score list
    score_lst = []
    for i in student_list:
        score_lst.append(i[1])
    print(score_lst)
    score_unique = sorted(list(set(score_lst)))
    print(score_unique)

    #second-lowest score
    second_lowest = score_unique[1]
    print(second_lowest)

    #creating names list with second-lowest score
    name_lst= []
    for i in student_list:
        if not second_lowest in i:
            continue
        name_lst.append(i[0])
    name_lst.sort()
    print(name_lst)

    #printing the names
    for i in name_lst:
        print(i)


if __name__ == '__main__':
    student_list= []
    for _ in range(int(input('How many students?: '))):
        name= input('Enter name: ')
        score= float(input('Enter score: '))
        student_list.append([name,score])
    runner_up()



