# Quiz questions and options
questions = [
    "Which command can be used to check the version of Python installed on your system?",
    "Which command is used to install a Python package using pip?",
    "How do you uninstall a Python package using pip?",
    "Which command can be used to list installed Python packages?",
    "What command is used to run a Python script from the terminal?",
    "Which command is used to create a new Python script file in the terminal?",
    "How can you display the contents of a Python script file in the terminal?",
    "Which command can be used to navigate to a specific directory in the terminal?",
    "True or False: In Windows, you use 'pip3' instead of 'pip' for Python 3 installations."
]

options = [
    ["A) python --version", "B) py --version", "C) python -v", "D) version python"],
    ["A) install package_name", "B) pip install package_name", "C) python install package_name", "D) package_name install"],
    ["A) uninstall package_name", "B) pip remove package_name", "C) pip uninstall package_name", "D) remove package_name"],
    ["A) list packages", "B) pip list", "C) show packages", "D) packages list"],
    ["A) run script.py", "B) execute script.py", "C) python script.py", "D) start script.py"],
    ["A) touch script.py", "B) create script.py", "C) python script.py", "D) new script.py"],
    ["A) print script.py", "B) display script.py", "C) cat script.py", "D) show script.py"],
    ["A) cd directory_name", "B) change directory_name", "C) goto directory_name", "D) move directory_name"],
    ["A) True", "B) False"]
]

# Corresponding answers
answers = ["A", "B", "C", "B", "C", "A", "C", "A", "B"]

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
