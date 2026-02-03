"""
so it is a rock paper scissor game in which we have 3 condition
If user choose Rock:
Rock- Rock= Draw
Rock-Paper= Paper
Rock-Scissor= Rock
If user choose Paper:
Paper-Paper= Draw
Paper- Rock=Paper
Paper-Scissor= Scissor
If user choose Scissor
Scissor- Scissor= Draw
Scissor- Paper= Scissor
Scissor- Rock=Rock
"""
import random
item_list=["Rock", "Paper","Scissor"]
user_choice=input("Select Item from List- Rock, Paper, Scissor: ")
comp_choice=random.choice(item_list)
print(f"User Choice: {user_choice}, Computer Choice: {comp_choice}")
if user_choice==comp_choice:
    print("Draw")
elif user_choice=="Rock":
    if comp_choice=="Paper":
        print("Paper wins")
    elif comp_choice=="Scissor":
        print("Rock Wins")
elif user_choice=="Paper":
    if comp_choice=="Rock":
        print("Paper wins")
    elif comp_choice=="Scissor":
        print("Scissor wins")
elif user_choice=="Scissor":
    if comp_choice=="Paper":
        print("Scissor wins")
    elif comp_choice=="Rock":
        print("Rock wins")