# The Grade Analyzer
# Objective:
# The aim of this assignment is to analyze a set of grades and provide statistics.

# Task 1: Code a function to calculate the average grade.
# Task 2: Implement a function to find the highest and lowest grade.
# Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
grades=[3,4,1,4,5]

def average(grades):
    average=int(sum(grades))//int(len(grades))
    print(f"The average is {average}") 
def low_high(grades):
   print(f"Here is the lowest grade {min(grades)} and the highest grade {max(grades)}")
    
def grade_letters(grades):
    grade_letters=[]
    for i in range(len(grades)):
        if grades[i] <=4:
            grade_letters.append("F")
        elif grades[i]<=5 or [i]<=6:
            grade_letters.append("D")        
        elif grades[i]<=6 or [i]<=7:
            grade_letters.append("C")
        elif grades[i]<=8 or [i]<=9:
            grade_letters.append("B")
        elif grades[i]==10:
            grade_letters.append("A")
    print(f"Here is a fixed list with the letter grades {grade_letters}")
            
average(grades)
low_high(grades)
grade_letters(grades)

    
        