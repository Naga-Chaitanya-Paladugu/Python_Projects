# Given the participants' score-sheet for your University Sports Day, you are required to find
# the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

# Sample Input
#
# 5
# 2 3 6 6 5
#
# Sample Output
#
# 5

def runner_up_score():
    arr_list= list(arr)
    print(arr_list)
    runner_up_list = list(set(arr_list))
    runner_up= sorted(runner_up_list, reverse=True)[1]
    print(runner_up)

    #Method 2
    # arr_sorted_lst= sorted(arr_list, reverse=True)
    # winner = arr_sorted_lst[0]
    # for i in arr_sorted_lst[1:]:
    #     if i == winner:
    #         continue
    #     runner= i
    #     print(f'The runner is {runner}')
    #     quit()

    #Method 3

    #importing counter library to get unique counts of scores
    # from collections import Counter
    # counter= Counter(arr_list)
    # score_dict= dict(counter)
    # print(score_dict)
    # score_list= list(score_dict.keys())
    # runner_up = sorted(score_list, reverse=True)[1]
    # print(f"The runner up is {runner_up}")



if __name__ == '__main__':
    n = int(input('Enter the total player count: '))
    arr= map(int, input("Enter each player's score with spaces: ").split())
    runner_up_score()