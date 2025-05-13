questions = {
    "What is the capital of India?": "new delhi",
    "What is 5 + 7?": "12",
    "Which language is this script written in?": "python"
}

score = 0
for question, answer in questions.items():
    user_answer = input(question + " ").lower()
    if user_answer == answer:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
print(f"Your final score is {score}/{len(questions)}.")

