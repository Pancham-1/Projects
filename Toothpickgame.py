print(" *** WELCOME TO THE TOOTHPICK GAME ***")
print("-"*50)
print(" Rules are simple :\n There are 2 players, each player can select 1,2 or 3 toothpicks at a time.\n The player picking the last toothpick wins !!! ")

num_left=13
player_1_name=input("Enter Player 1's name : ")
player_2_name=input("Enter Player 2's name : ")
current_player=player_1_name

while True: 
 print("| "*num_left)
 print(f" There are {num_left} toothpicks left")
 choice = int(input(f"{current_player}, how many toothpicks do you pick ?"))
 while choice!=1 and choice!=2 and choice!=3:
   choice=int(input(f"{current_player}, you can only choose 1,2,3:"))
 num_left-=choice
 if num_left<=0:
    print(f"{current_player} Wins the Game")
    break
 if current_player==player_1_name:
   current_player = player_2_name
else:
  current_player=player_1_name

 
print("GAME OVER")
print("-"*50)
