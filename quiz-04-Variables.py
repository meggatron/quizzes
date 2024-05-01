# Assigning variables
age = 30
name = "John"
price = 19.99
is_student = True
fruits = ["apple", "banana", "cherry"]
person = {"name": "Alice", "age": 25}

print("Variables assigned:")
print(f"age = {age}")
print(f"name = '{name}'")
print(f"price = {price}")
print(f"is_student = {is_student}")
print(f"fruits = {fruits}")
print(f"person = {person}")
print()

# Quiz questions
questions = [
    "What data type is the variable 'age'?",
    "What is the value of the variable 'name'?",
    "What data type is the variable 'price'?",
    "What is the value of the variable 'is_student'?",
    "What data type is the variable 'fruits'?",
    "What is the value of the variable 'person'?"
]

# Corresponding answers
answers = [
    ["int", "integer"],
    "John",
    ["float", "floating-point number"],
    "True",
    "list",
    "dictionary"
]

# Function to run the quiz
def run_quiz(questions, answers):
    score = 0
    total_questions = len(questions)
    for i in range(total_questions):
        print(f"Question {i+1}: {questions[i]}")
        user_answer = input("Your answer: ").strip()
        correct_answers = answers[i] if isinstance(answers[i], list) else [answers[i]]
        if user_answer.lower() in map(str.lower, correct_answers):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {', '.join(str(answer) for answer in correct_answers)}")
        print()
    print(f"You got {score} out of {total_questions} correct.")

# Run the quiz
run_quiz(questions, answers)
