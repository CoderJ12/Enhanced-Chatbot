import random
import time

choices = ["rock", "paper", "scissors"]

user_score = 0
ai_score = 0

def get_ai_choice():
    return random.choice(choices)

def decide_winner(user, ai):
    global user_score, ai_score

    if user == ai:
        return "It's a tie!"

    elif (user == "rock" and ai == "scissors") or \
         (user == "paper" and ai == "rock") or \
         (user == "scissors" and ai == "paper"):
        user_score += 1
        return "You win this round!"

    else:
        ai_score += 1
        return "AI wins this round!"

def show_points():
    print(f"Score → You: {user_score} | AI: {ai_score}")
    print("-" * 30)

def play_game():
    while True:
        user_choice = input(
            "Enter rock, paper, scissors, 'pt' (points), or 'q' (quit): "
        ).lower()

        if user_choice == 'q':
            print("\nFinal Score:")
            show_points()
            print("Thanks for playing!")
            break

        elif user_choice == 'pt':
            show_points()
            continue

        elif user_choice not in choices:
            print("Invalid choice, try again.")
            continue

        ai_choice = get_ai_choice()
        print(f"AI chose: {ai_choice}")

        result = decide_winner(user_choice, ai_choice)
        print(result)

        print("-" * 30)

play_game()