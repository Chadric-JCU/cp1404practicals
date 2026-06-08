

import scores

MENU = "(G)et score\n(P)rint result\n(S)how stars\n(Q)uit"
MINIMUM_SCORE, MAXIMUM_SCORE = 0, 100 #Minimum and maximum value for scores respectively

def main():
    """A menu to get a valid score, print the result and print number of stars based on the score"""

    score=validate_score(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = validate_score(MINIMUM_SCORE, MAXIMUM_SCORE)

        elif choice == "P":
            grade = scores.determine_grade(score)
            print(f"Score {score} is {grade}")

        elif choice == "S":
            print_stars(score)

        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ").upper()
    print("Exiting program, goodbye.")


def print_stars(score: int):
    for i in range(score):
        print("*", end="")
    print("")


def validate_score(minimum, maximum):
    score = int(input("Enter a score between 0 and 100 inclusive\n>>> "))
    while score<minimum or score>maximum:
        print("Invalid score!")
        score = int(input("Enter a score between 0 and 100 inclusive\n>>> "))
    return score


main()