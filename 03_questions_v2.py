import random


def choice_checker(question, valid_list, error):
    while True:
        # Ask user for choice
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)


def check_questions():
    while True:
        response = input("how many questions: ")

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


questions = check_questions()
questions_played = 0
end_game = "no"
while end_game == "no":
    print()
    if questions == "":
        heading = "Continuous mode: " \
                  "Round {}".format(questions_played + 1)
    else:
        heading = "Questions {} of " \
                  "{}".format(questions_played + 1, questions)

    print(heading)
    choose_instruction = "Please choose easy (e), medium " \
                         "(m), or hard (h), " \
                         "or 'xxx' to exit: "

    difficulty = ['easy', 'medium', 'hard', 'xxx']

    choose_error = "Please choose from easy / " \
                   "medium / hard (or xxx to quit)"

    user_level = choice_checker(choose_instruction, difficulty, choose_error)

    print(f"You have selected {user_level} mode.")

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

    question = f"{num1} {operator1} {num2} {operator2} {num3}"
    answer = eval(question)

    print("Question:", question)
    print("Start Answering!!")
    print() 

