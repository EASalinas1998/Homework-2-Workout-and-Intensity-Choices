#########################
# CSCI 1380.04
# Spring 2022
# Homework 02
# Eduardo Salinas
#########################

# Declares {exercise_type} and prompts the user to input based on the text.
exercise_type = input("Enter the type of exercise: ")

# Declares {difficulty_level}, formatted it to integer, and prompts the user to input based on the text.
difficulty_level = int(input("Enter the difficulty level: "))

# If {exercise_type} is arms and difficulty_level is 1-4, displays to the user the exercise regimen based on the difficulty level. If difficulty is not 1-4, then "Invalid difficulty level" is displayed.
if exercise_type == "arms":

  if difficulty_level == 1:
    print("Back Press: 6 reps")
    print("Bow Pull: 4 reps (left), 4 reps (right)")
    print("Front Press: 6 reps")
    print("Overhead Arm Spin: 15 reps")
    print("Overhead Arm Twist: 39 reps")
    print("Overhead Press: 6 reps")
    print("Shoulder Press: 4 reps (left), 4 reps (right)")
    print("Tricep Kickback: 4 reps (left), 4 reps (right)")
  
  elif difficulty_level == 2:
    print("Back Press: 14 reps")
    print("Bow Pull: 10 reps (left), 10 reps (right)")
    print("Front Press: 14 reps")
    print("Overhead Arm Spin: 20 reps")
    print("Overhead Arm Twist: 43 reps")
    print("Overhead Press: 14 reps")
    print("Shoulder Press: 10 reps (left), 10 reps (right)")
    print("Tricep Kickback: 10 reps (left), 10 reps (right)")
  
  elif difficulty_level == 3:
    print("Back Press: 24 reps")
    print("Bow Pull: 15 reps (left), 15 reps (right)")
    print("Front Press: 24 reps")
    print("Overhead Arm Spin: 27 reps")
    print("Overhead Arm Twist: 48 reps")
    print("Overhead Press: 24 reps")
    print("Shoulder Press: 15 reps (left), 15 reps (right)")
    print("Tricep Kickback: 15 reps (left), 15 reps (right)")
  
  elif difficulty_level == 4:
    print("Back Press: 37 reps")
    print("Bow Pull: 24 reps (left), 24 reps (right)")
    print("Front Press: 37 reps")
    print("Overhead Arm Spin: 60 reps")
    print("Overhead Arm Twist: 60 reps")
    print("Overhead Press: 37 reps")
    print("Shoulder Press: 24 reps (left), 24 reps (right)")
    print("Tricep Kickback: 24 reps (left), 24 reps (right)")
  
  else:
    print("Invalid difficulty level")

# If {exercise_type} is legs and difficulty_level is 1-4, displays to the user the exercise regimen based on the difficulty level. If difficulty is not 1-4, then "Invalid difficulty level" is displayed.
elif exercise_type == "legs":

  if difficulty_level == 1:
    print("Hip Lift: 6 reps")
    print("Knee Lift: 25 reps")
    print("Knee Lift-Combo: 25 reps")
    print("Mountain Climber: 15 reps")
    print("Overhead Squat: 6 reps")
    print("Ring Raise Combo: 25 reps")
    print("Side Step: 6 reps")
    print("Squat: 6 reps")
    print("Thigh Press: 6 reps")
    print("Wide Squat: 6 reps")

  elif difficulty_level == 2:
    print("Hip Lift: 14 reps")
    print("Knee Lift: 30 reps")
    print("Knee Lift-Combo: 30 reps")
    print("Mountain Climber: 20 reps")
    print("Overhead Squat: 14 reps")
    print("Ring Raise Combo: 30 reps")
    print("Side Step: 30 reps")
    print("Squat: 14 reps")
    print("Thigh Press: 14 reps")
    print("Wide Squat: 14 reps")

  elif difficulty_level == 3:
    print("Hip Lift: 24 reps")
    print("Knee Lift: 37 reps")
    print("Knee Lift-Combo: 37 reps")
    print("Mountain Climber: 27 reps")
    print("Overhead Squat: 24 reps")
    print("Ring Raise Combo: 37 reps")
    print("Side Step: 37 reps")
    print("Squat: 24 reps")
    print("Thigh Press: 24 reps")
    print("Wide Squat: 24 reps")

  elif difficulty_level == 4:
    print("Hip Lift: 37 reps")
    print("Knee Lift: 60 reps")
    print("Knee Lift-Combo: 60 reps")
    print("Mountain Climber: 60 reps")
    print("Overhead Squat: 37 reps")
    print("Ring Raise Combo: 60 reps")
    print("Side Step: 60 reps")
    print("Squat: 37 reps")
    print("Thigh Press: 37 reps")
    print("Wide Squat: 37 reps")

  else:
    print("Invalid difficulty level")

# If {exercise_type} is core and difficulty_level is 1-4, displays to the user the exercise regimen based on the difficulty level. If difficulty is not 1-4, then "Invalid difficulty level" is displayed.
elif exercise_type == "core":

  if difficulty_level == 1:
    print("Flutter Kick: 25 reps")
    print("Knee-to-Chest: 6 reps")
    print("Leg Raise: 5 reps")
    print("Leg Scissors: 25 reps")
    print("Open & Close Leg Raise: 5 reps")
    print("Overhead Bend: 6 reps")
    print("Overhead Hip Shake: 39 reps")
    print("Overhead Lunge Twist: 4 reps (left), 4 reps (right)")
    print("Overhead Side Bend: 6 reps")
    print("Pendulum Bend: 6 reps")
    print("Plank: 4 reps")
    print("Russian Twist: 25 reps")
    print("Seated Forward Press: 6 reps")
    print("Seated Ring Raise: 25 reps")
    print("Standing Twist: 25 reps")

  elif difficulty_level == 2:
    print("Flutter Kick: 30 reps")
    print("Knee-to-Chest: 14 reps")
    print("Leg Raise: 13 reps")
    print("Leg Scissors: 30 reps")
    print("Open & Close Leg Raise: 13 reps")
    print("Overhead Bend: 14 reps")
    print("Overhead Hip Shake: 43 reps")
    print("Overhead Lunge Twist: 10 reps (left), 10 reps (right)")
    print("Overhead Side Bend: 14 reps")
    print("Pendulum Bend: 14 reps")
    print("Plank: 11 reps")
    print("Russian Twist: 30 reps")
    print("Seated Forward Press: 14 reps")
    print("Seated Ring Raise: 30 reps")
    print("Standing Twist: 30 reps")
    
  elif difficulty_level == 3:
    print("Flutter Kick: 37 reps")
    print("Knee-to-Chest: 24 reps")
    print("Leg Raise: 22 reps")
    print("Leg Scissors: 37 reps")
    print("Open & Close Leg Raise: 22 reps")
    print("Overhead Bend: 24 reps")
    print("Overhead Hip Shake: 48 reps")
    print("Overhead Lunge Twist: 15 reps (left), 15 reps (right)")
    print("Overhead Side Bend: 24 reps")
    print("Pendulum Bend: 24 reps")
    print("Plank: 19 reps")
    print("Russian Twist: 37 reps")
    print("Seated Forward Press: 24 reps")
    print("Seated Ring Raise: 37 reps")
    print("Standing Twist: 37 reps")

  elif difficulty_level == 4:
    print("Flutter Kick: 60 reps")
    print("Knee-to-Chest: 37 reps")
    print("Leg Raise: 33 reps")
    print("Leg Scissors: 60 reps")
    print("Open & Close Leg Raise: 33 reps")
    print("Overhead Bend: 37 reps")
    print("Overhead Hip Shake: 60 reps")
    print("Overhead Lunge Twist: 24 reps (left), 24 reps (right)")
    print("Overhead Side Bend: 37 reps")
    print("Pendulum Bend: 37 reps")
    print("Plank: 30 reps")
    print("Russian Twist: 60 reps")
    print("Seated Forward Press: 37 reps")
    print("Seated Ring Raise: 60 reps")
    print("Standing Twist: 60 reps")

  else:
    print("Invalid difficulty level")

# If {exercise_type} is yoga and difficulty_level is 1-4, displays to the user the exercise regimen based on the difficulty level. If difficulty is not 1-4, then "Invalid difficulty level" is displayed.
elif exercise_type == "yoga":

  if difficulty_level == 1:
    print("Boat Pose: 4 reps")
    print("Chair Pose: 4 reps")
    print("Fan Pose: 4 reps (left), 4 reps (right)")
    print("Hinge Pose: 4 reps (left), 4 reps (right)")
    print("Revolved Crescent Lunge Pose: 4 reps (left), 4 reps (right)")
    print("Standing Forward Fold: 4 reps")
    print("Tree Pose: 4 reps (left), 4 reps (right)")
    print("Warrior I Pose: 4 reps (left), 4 reps (right)")
    print("Warrior II Pose: 4 reps (left), 4 reps (right)")
    print("Warrior III Pose: 4 reps (left), 4 reps (right)")

  elif difficulty_level == 2:
    print("Boat Pose: 6 reps")
    print("Chair Pose: 6 reps")
    print("Fan Pose: 6 reps (left), 6 reps (right)")
    print("Hinge Pose: 6 reps (left), 6 reps (right)")
    print("Revolved Crescent Lunge Pose: 6 reps (left), 6 reps (right)")
    print("Standing Forward Fold: 6 reps")
    print("Tree Pose: 6 reps (left), 6 reps (right)")
    print("Warrior I Pose: 6 reps (left), 6 reps (right)")
    print("Warrior II Pose: 6 reps (left), 6 reps (right)")
    print("Warrior III Pose: 6 reps (left), 6 reps (right)")

  elif difficulty_level == 3:
    print("Boat Pose: 8 reps")
    print("Chair Pose: 8 reps")
    print("Fan Pose: 6 reps (left), 6 reps (right)")
    print("Hinge Pose: 6 reps (left), 6 reps (right)")
    print("Revolved Crescent Lunge Pose: 6 reps (left), 6 reps (right)")
    print("Standing Forward Fold: 8 reps")
    print("Tree Pose: 6 reps (left), 6 reps (right)")
    print("Warrior I Pose: 6 reps (left), 6 reps (right)")
    print("Warrior II Pose: 6 reps (left), 6 reps (right)")
    print("Warrior III Pose: 6 reps (left), 6 reps (right)")

  elif difficulty_level == 4:
    print("Boat Pose: 16 reps")
    print("Chair Pose: 16 reps")
    print("Fan Pose: 14 reps (left), 14 reps (right)")
    print("Hinge Pose: 14 reps (left), 14 reps (right)")
    print("Revolved Crescent Lunge Pose: 14 reps (left), 14 reps (right)")
    print("Standing Forward Fold: 16 reps")
    print("Tree Pose: 14 reps (left), 14 reps (right)")
    print("Warrior I Pose: 14 reps (left), 14 reps (right)")
    print("Warrior II Pose: 14 reps (left), 14 reps (right)")
    print("Warrior III Pose: 14 reps (left), 14 reps (right)")

  else:
    print("Invalid difficulty level")

# If {exercise_type} is not of the correct listed in lowercase formatting, then "Invalid type of exercise" is displayed.
else:
  print("Invalid type of exercise")