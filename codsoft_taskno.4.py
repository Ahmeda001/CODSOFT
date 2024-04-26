import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_again():
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ['yes', 'no']:
            return play_again == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    user_score = 0
    computer_score = 0
    while True:
        print("\n--- Let's play Rock-Paper-Scissors! ---")
        user_choice = get_user_choice()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
