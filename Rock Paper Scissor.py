import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock-Paper-Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        # Get user input
        user_choice_num = input("Enter your choice (1-3) or 4 to quit: ")

        if user_choice_num == '4':
            break

        if user_choice_num not in ['1', '2', '3']:
            print("Invalid choice. Please enter 1, 2, 3, or 4 to quit.")
            continue

        # Map user input to actual choices
        choices = {1: "rock", 2: "paper", 3: "scissors"}
        user_choice = choices[int(user_choice_num)]

        # Generate computer choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)

        # Update scores
        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        # Display the result
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(result)
        print(f"Score - You: {user_score}, Computer: {computer_score}")

    print("Thanks for playing!")

# Run the game
rock_paper_scissors_game()
