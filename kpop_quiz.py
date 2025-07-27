# K-Pop Quiz Game
print("Welcome to the K-Pop Quiz!")
score = 0

question1 = input("Which group does Jeonghan belong to? ")
if question1.lower() == "seventeen":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is SEVENTEEN.")

question2 = input("Who is the leader of BTS? ")
if question2.lower() == "rm":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is RM.")

question3 = input("Which year did BLACKPINK debut? ")
if question3 == "2016":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 2016.")

print(f"Your final score is {score}/3")
