# Assigning an integer to a variable
age = 30
# Assigning a string to a variable
name = "John"
# Assigning a floating-point number to a variable
price = 19.99
# Assigning a boolean value to a variable
is_student = True
# Assigning a list to a variable
fruits = ["apple", "banana", "cherry"]
# Assigning a dictionary to a variable
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
    "integer",
    "John",
    "floating-point number",
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
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == answers[i].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is '{answers[i]}'")
        print()
    print(f"You got {score} out of {total_questions} correct.")

# Run the quiz
run_quiz(questions, answers)
