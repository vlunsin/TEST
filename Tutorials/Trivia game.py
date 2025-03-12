# List of questions
# Store the answers
# Randomly pick some questions
# ask the questions 
# see if they are correct
# keep track of the score
# tell the user the score

# Dictionnary for questions 
questions = {
    "Q1": "A1",
    "Q2": "A2",
    "Q3": "A3",
    "Q4": "A4",
    "Q25": "A25",
    "Q37": "A37"
}

import random

# function to call the game. Resuable part of code
def python_trivia_game():
    print("Hello")
    # for a list, keys or values
    questions_list = list(questions.keys())
    total_questions = 3
    score = 0
    selected_questions = random.sample(questions_list, total_questions)
    print(selected_questions)

# to get index of question, as well as value
    for idx, question in enumerate(selected_questions):
        # f string to format 
        print(f"{idx + 1}. {question}")
        # input to allow user to type in terminal
        # lower to make answer lower case
        # strip to remove the space before and after, good to use on user input
        user_answer = input("Your answer: ").lower().strip()

# need to compare to correct answer
        # will give the associate value for the key question in the list questions
        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            # \n to go to next line
            print("Correct\n")
            score += 1
        else:    
            print(f"Wrong. The correct answer is: {correct_answer}.\n")

# Score
        print(f"Game over. The final score is: {score}/{total_questions}")


# To use, call the function
python_trivia_game()

