# Importing necessary libraries
import random

# List of questions, options, and answers
questions = [
    "What symbol is used to assign a value to a variable in Python?",
    "What is the correct syntax to declare a variable in Python?",
    "Which of the following is a valid variable name in Python?",
    "What will be the value of x after the following code executes?\n\nx = 5\nx = x + 2"
]

options = [
    ["A. =", "B. :", "C. ->", "D. -="],
    ["A. var x", "B. int x", "C. x = 5", "D. x: int = 5"],
    ["A. 2var", "B. _var", "C. var-2", "D. my_var"],
    ["A. 5", "B. 7", "C. 2", "D. None of the above"]
]

answers = ["A", "C", "D", "B"]

# Function to shuffle the questions
def shuffle_questions():
    combined = list(zip(questions, options, answers))
    random.shuffle(combined)
    return zip(*combined)

# Function to display questions and options, and check answers
def display_question(question, options):
    print(question)
    for option in options:
        print(option)

# Main function to run the quiz
def main():
    shuffled_questions, shuffled_options, shuffled_answers = shuffle_questions()
    score = 0
    for i in range(len(shuffled_questions)):
        display_question(shuffled_questions[i], shuffled_options[i])
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        if user_answer == shuffled_answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print("You got {} out of {} questions correct.".format(score, len(shuffled_questions)))

if __name__ == "__main__":
    main()
