# 5. The Fitness Tracker
# Objective:
# The aim of this assignment is to create a program that tracks fitness activities and calories burned.







# Task 1: 
activities=["Dancing", "Swimming", "Biking"]  
duration = [10, 20, 15]

# Task 2:
def calories():
    activity = input("Choose you activity: Dancing, Swimming or Biking: ")
    i = activities.index(activity)
    caloriesburned = duration[i]*3.5
    print(caloriesburned)

# Task 3:
def summary():
    for i in range(len(activities)):
        print(f"Total calories burned with {activities[i]}: {duration[i]*3.5}")
    print(f"If you participated in all the activities, the total is: {sum(duration)*3.5}")

    
calories()
summary()          
