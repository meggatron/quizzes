# Quiz questions and options
questions = [
    "Which command can be used to check the version of Python installed on your system?",
    "Which command is used to install a Python package using pip?",
    "Which command is used to navigate to a specific directory in the terminal?"
]

options = [
    ["A) python --version", "B) py --version", "C) python -v", "D) version python"],
    ["A) install package_name", "B) pip install package_name", "C) python install package_name", "D) package_name install"],
    ["A) cd directory_name", "B) change directory_name", "C) goto directory_name", "D) move directory_name"]
]

# Corresponding answers
answers = ["A", "B", "A"]

# Function to run the quiz
def run_quiz(questions, options, answers):
    score = 0
    total_questions = len(questions)
    for i in range(total_questions):
        print(f"Question {i+1}: {questions[i]}")
        for option in options[i]:
            print(option)
        user_answer = input("Your answer: ").strip().upper()
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is '{answers[i]}'")
        print()
    print(f"You got {score} out of {total_questions} correct.")

# Run the quiz
run_quiz(questions, options, answers)
