# K-Pop Quiz Game (Improved Version)
import time
from colorama import Fore, Style

def play_quiz():
    print(Fore.CYAN + "Welcome to the K-Pop Quiz!" + Style.RESET_ALL)
    print("Answer the questions and test your K-Pop knowledge!")
    print("-" * 40)
    score = 0

    # Questions
    questions = [
        ("Which group does Jeonghan belong to?", "seventeen"),
        ("Who is the leader of BTS?", "rm"),
        ("Which year did BLACKPINK debut?", "2016"),
        ("Which group released the song 'Love Dive'?", "ive"),
        ("Who is the maknae of TWICE?", "tzuyu")
    ]

    # Ask questions
    for q, a in questions:
        answer = input(Fore.YELLOW + q + " " + Style.RESET_ALL).lower()
        if answer == a:
            print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
            score += 1
        else:
            print(Fore.RED + f"Wrong! The correct answer is {a.capitalize()}." + Style.RESET_ALL)
        time.sleep(0.5)

    # Final Score
    percentage = (score / len(questions)) * 100
    print("-" * 40)
    print(Fore.CYAN + f"Your final score is {score}/{len(questions)} ({percentage:.2f}%)" + Style.RESET_ALL)

# Main game loop
while True:
    play_quiz()
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print(Fore.MAGENTA + "Thanks for playing! Goodbye!" + Style.RESET_ALL)
        break
