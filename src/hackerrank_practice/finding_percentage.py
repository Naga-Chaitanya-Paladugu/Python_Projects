def average_score(name):
    print(student_profile[name])
    student_avg= sum(student_profile[name])/len(student_profile[name])
    print(f"{name}'s average is {student_avg}")

if __name__ == '__main__':
    #Testing dictionary
    student_profile= {'ja': [2, 3, 4], 'ka': [4, 5, 6], 'la': [6, 7, 7]}

    # student_profile= {}
    # for _ in range(int(input('Enter the number of student profiles: '))):
    #     info = input('Enter the name and scores: ').split()
    #     for i in range(1):
    #         student_profile[info[i]] = [int(i) for i in info[i+1: ]]
    # print(student_profile)
    query_name = input('Enter the name of the student for calculating average score: ')
    average_score(query_name)


