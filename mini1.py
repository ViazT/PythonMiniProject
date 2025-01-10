import random 

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)

    return roll

while True  :
    players = input("Enter number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:

            break
        else: 
             print("Invalid number of players. Please enter 2-4 players.")
    else:
            print("Invalid number of players. Please enter a number between 2 and 4.")

max_score = 50
players_scored = [ 0 for _ in range(players)] 

while max(players_scored) < max_score:
    for i in range(players):
        print(f"\nPlayer {i+1}'s turn\n") 
        print(f"Your total score is: {players_scored[i]}\n")
        current_score = 0
        while True:
            s_roll  = input("Would you want to roll (y)?: ")
            if s_roll.lower() != "y":
                break

            val = roll()
            if val == 1:
                current_score = 0
                print("You rolled a 1! You lose your turn.")
                break
            else:
                current_score += val
                print(f"You rolled a : {val}")
            print(f"Your current score is: {current_score}")
        players_scored[i] += current_score
        print(f"Your total score is: {players_scored[i]}")