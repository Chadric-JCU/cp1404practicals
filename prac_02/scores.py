"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

def main():
    score = float(input("Enter score: "))
    grade = determine_grade(score)
    print(f"User score {score} is {grade}")
    if grade == "Excellent":
        print("You get a prize!")
    random_score = random.randint(0, 100)
    grade = determine_grade(random_score)
    print(f"Random: {random_score} = {grade} ")

def determine_grade(score):
    if score < 0 or score > 100:
        grade = "Invalid score"
    elif score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade= "Passable"
    else:
        grade = "Bad"

    return grade

#main()