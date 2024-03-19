# 4. The Quiz Game
# Objective:
# The aim of this assignment is to create a quiz game that asks questions and checks answers.

# Task 1: Develop a list of questions and answers.
# Task 2: Write a function that quizzes the user and takes their answers.
# Task 3: Score the quiz and give the user feedback on their performance.
questions=["What is the actual year?","how much is 1+3?", "Who is your favorite alumn?"]
answers=["2024", "4", "Juan Medina"]
def correct_answers():
    score=0
    response=input(questions[0])
    if response!=answers[0]:
       print("Wrong answer!")
    elif response==answers[0]: 
        print("correct!")
        score+=1
    response=input(questions[1])
    if response!=answers[1]:
       print("Wrong answer!")
    elif response==answers[1]: 
        print("correct!")
        score+=1
    response=input(questions[2])
    if response!=answers[2]:
       print("Wrong answer!")
    elif response==answers[2]: 
        print("correct!")
        score+=1
    print(f"your score was: {score}/3")
correct_answers()