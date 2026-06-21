import random

print(" Rock Paper Scissors Game ")

user_score = 0
computer_score = 0

choices = ["rock",
            "paper",
              "scissors"]

while True:

    print("\nChoose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter your choice: ").lower()

    if user_choice not in choices:
        print("❌ Invalid choice! Please enter rock, paper, or scissors")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print(" It's a Draw!")

    elif (

        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You Win!")
        user_score += 1

    else:
        print("💻 Computer Wins!")
        computer_score += 1

    print("\nCurrent Score")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\nFinal Score ")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")

if user_score > computer_score:
    print(" Congratulations! You are the overall winner.")

elif computer_score > user_score:
    print(" Computer is the overall winner")

else:
    print("Match Draw!")

print("Thanks for playing!")