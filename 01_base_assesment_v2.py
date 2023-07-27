import random


# Functions go here...

# Function to get a yes or no response from the user
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            instructions()
            return "no"
        else:
            print("Please answer yes / no")


# Function to display game instructions
def instructions():
    print()
    print("***** How To Play *****")
    print("It's a math quiz.")
    print("There are 3 Modes/ Difficulties Easy medium and hard.")
    print("Easy will give you an addition and subtraction equation.")
    print("Medium will give you an multiplication equation.")
    print("Hard will give you an mix of all the above.")
    print("Try your best to answer all questions correct.")
    print("Have Fun :)")
    print()


# Function to validate user's choice
def choice_checker(question, valid_list, error):
    while True:
        # Ask user for choice
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)


# Function to check the number of questions
def check_questions():
    while True:
        response = input("how many questions or press <enter> to play infinite mode")

        question_error = "Please type either <enter> or an integer that is more than 0\n"

        # If infinite
        if response == "":
            return ""

        try:
            response = int(response)

            if response < 1:
                print(question_error)
                continue

        except ValueError:
            print(question_error)
            continue

        return response


# Function to check if the input is an integer within specified bounds
def int_check(question, low=None, high=None):
    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:
        try:
            response = int(input(question))

            # Check input is not too high or too low if both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between {} and {}".format(low, high))
                    continue

            # Check input is not too low
            elif situation == "low only":
                if response < low:
                    print("Please enter a number that is equal to or greater than {}".format(low))
                    continue

            return response

        except ValueError:
            print("Please enter an integer")
            continue


# Main routine goes here...
show_instructions = yes_no("Have you played this game before? ")

questions = check_questions()
questions_played = 0
questions_correct = 0
questions_incorrect = 0

# Rounds loop
end_game = "no"
while end_game == "no":
    print()
    # This code sees if the user has left it blank and press enter than the code will head into continuous mode
    # Otherwise it will get the users input and show them that they are (round number) of (how many rounds they wanted to play)
    if questions == "":
        heading = "Continuous mode: " \
                  "Round {}".format(questions_played + 1)
    else:
        heading = "Questions {} of " \
                  "{}".format(questions_played + 1, questions)
        print(heading)
    # User choose their difficulty for their question
    choose_instruction = "Please choose easy (e), medium " \
                         "(m), or hard (h), " \
                         "or 'xxx' to exit: "

    difficulty = ['easy', 'medium', 'hard', 'xxx']

    choose_error = "Please choose from easy / " \
                   "medium / hard (or xxx to quit)"
    # User can quit at this point but at no point when answering the question
    user_level = choice_checker(choose_instruction, difficulty, choose_error)
    if user_level == "xxx":
        break
    # tells user what mod they have selected
    print(f"You have selected {user_level} mode.")
    # Generate the question going off what the user's input was when choosing the difficulty
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    num3 = random.randint(1, 20)

    if user_level == "easy":
        operator1 = random.choice(["+"])
        operator2 = random.choice(["-"])
    elif user_level == "medium":
        operator1 = operator2 = random.choice(["*"])
    elif user_level == "hard":
        operator1 = random.choice(["+", "-"])
        operator2 = random.choice(["*"])
    # The question base and the solver
    question = f"{num1} {operator1} {num2} {operator2} {num3}"
    answer = eval(question)
    # prints the question
    print("Question:", question)
    print("Start Answering!!")
    print()
    # Prints the answer after the user has inputted an answer
    guess = int_check("Type in the answer!")
    print("You answered:", guess)
    if answer != guess:
        print("Answer: ", answer)

    # Compare guess to answer if answer is correct "Correct" if answer is wrong "Incorrect"
    if guess == answer:
        print("Correct!")
        questions_correct += 1
    else:
        print("Incorrect!")
        questions_incorrect += 1

    questions_played += 1

    # Check if we are out of rounds
    if questions_played == questions:
        break

Quiz_summary = []

# Calculate Game Stats
questions_correct = questions_played - questions_incorrect

# Calculate percentages
if questions_played > 0:
    percent_correct = questions_correct / questions_played * 100
    percent_incorrect = questions_incorrect / questions_played * 100
else:
    percent_correct = 0
    percent_incorrect = 0

print()

# Display game stats with values rounded to the nearest whole number
print("******* Game Statistics *******")
print(
    "Correct: {}, ({:.0f}%)\n Incorrect: {}, ({:.0f}%)".format(questions_correct, percent_correct, questions_incorrect,
                                                               percent_incorrect))
