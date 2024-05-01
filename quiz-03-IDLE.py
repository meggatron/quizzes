# Quiz questions and options
questions = [
    "What is the first step to begin writing Python code using IDLE?",
    "What action should you take after opening the IDLE application?",
    "What is the purpose of the following Python code snippet? \nword = 'abracadabra' \nfor i in range(len(word)): \n   print(word[:len(word)-i])\n "
]

options = [
    ["A) Open the IDLE application", "B) Click on the 'File' menu", "C) Type your Python code", "D) Save the file"],
    ["A) Type your Python code directly", "B) Click on the 'File' menu", "C) Run the Python interpreter", "D) Close the application"],
    ["A) It prints a series of numbers.", "B) It calculates the factorial of a number.", "C) It prints substrings of a word.", "D) It defines a function to reverse a string."]
]

# Corresponding answers
answers = ["A", "B", "C"]

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
