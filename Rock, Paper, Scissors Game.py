import random

picks = ["rock", "paper", "scissors"]
user_wins = 0
system_wins = 0

while True:
    user_pick = input("Type rock, paper or scissors or type q to quit\n").lower()
    if user_pick == "q":
        break

    if user_pick not in picks:
        continue

    random_number = random.randint(0, 2)
    system_pick = picks[random_number]
    print("System picked", system_pick + ". ")

    if user_pick == "rock" and system_pick == "scissors":
        print("You win!")
        user_wins += 2
    elif user_pick == "paper" and system_pick == "rock":
        print("You win!")
        user_wins += 2
    elif user_pick == "scissors" and system_pick == "paper":
        print("You win!")
        user_wins += 2
    else:
        print("You lost!")
        system_wins += 2

print("You won", user_wins, "times.")
print("System won", system_wins, "times.")
print("\nGoodbye!")