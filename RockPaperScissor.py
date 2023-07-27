
rock="""
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper="""
 _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
 _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


from random import randint
num = randint(1,3)



if num == 1:
    ComputerMove= "rock"
elif num== 2:
    ComputerMove="paper"
elif num==3:
    ComputerMove="scissors"



print("-"*20)
print(" *** WELCOME TO ROCK , PAPER AND SCISSORS GAME *** ")



Player_move = input("Enter your move(rock,paper,scissors) : ").lower()


print("Your Move:")


if Player_move=="rock":
    print(rock)
elif Player_move=="paper":
    print(paper)
elif Player_move=="scissors":
    print(scissors)


print("Computer Move:")


if ComputerMove=="rock":
    print(rock)
elif ComputerMove=="paper":
    print(paper)
elif ComputerMove=="scissors":
    print(scissors)


if ComputerMove==Player_move:
    print(" IT'S A TIE !!!")
elif ComputerMove=="rock" and Player_move=="paper":
    print(" Yeah !!! You Win")
elif ComputerMove=="paper" and Player_move=="scissors":
    print(" Yeah !!! You Win")
elif ComputerMove=="scissors" and Player_move=="rock":
    print(" Yeah !!! You Win")
else:
    print(" You Lose...")


#Please don't type anything other than rock, paper, scissors but if you do your defeat is inevitable.
# This exercise really helped me to organise my thoughts in making the game in a systematic order. ASCII art is pretty cool, RIGHT!
