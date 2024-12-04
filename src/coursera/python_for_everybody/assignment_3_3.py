# #3.3 Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error. If the score is between 0.0 and 1.0,
# print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit.
# For the test, enter a score of 0.85.


def score_calculator(score: float):
        if score<0 or score> 1:
            print('Please enter a valid score between 0.0 and 1.0')
            quit()
        elif score >= 0.9:
            print('Your score is: A')
        elif score >= 0.8:
            print('Your score is: B')
        elif score >= 0.7:
            print('Your score is: C')
        elif score >= 0.6:
            print('Your score is: D')
        else:
            print('Your score is: F')


if __name__ == '__main__':
    try:
        score = float(input("Enter your score: "))
        score_calculator(score)
    except ValueError:
        print('Invalid input. Please enter a valid numeric input')
