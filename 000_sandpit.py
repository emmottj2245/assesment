import random


# Functions go here...

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return instructions()

        else:
            print("Please answer yes / no")


def instructions():
    print()
    print("***** How To Play *****")
    print()
    print("it's a math game")
    print("You should try and improve your maths skills. ")
    print("Have Fun :)")
    print()


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

        question_error = "Please type either <enter> " \
                         " or an integer that is more than 0\n"
        # If infinite
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(question_error)
                    continue

            except ValueError:
                print(question_error)
                continue

        return response


def int_check(question, low=None, high=None):
    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            # checks input is not too high or too low if a both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number that is more that {} and {}".format(low, high))
                    continue

            # check input is not too low
            elif situation == "low only":
                if response < low:
                    print("please enter a number that is more than (or equal to) {}".format(low))

                    continue

            return response

        # check input is an integer

        except ValueError:
            print("please enter an integer")
            continue


# main routine goes here...
show_instructions = yes_no("have you played this game"
                           " before? ")

questions = check_questions()
questions_played = 0
questions_won = 0
questions_lost = 0

# rounds loop
end_game = "no"
while end_game == "no":

    print()
    if questions == "":
        heading = "Continuous mode: " \
                  "Round {}".format(questions_played + 1)
    else:
        heading = "questions {} of " \
                  "{}".format(questions_played + 1, questions)

    print(heading)
    choose_instruction = "Please choose easy (e), medium " \
                         "(m) or hard (h)" \
                         "or 'xxx' to exit: "
    choose_error = "Please choose from easy / " \
                   "medium / hard (or xxx to quit)"

    difficulty = ['easy', 'medium', 'hard', 'xxx']

    user_choice = choice_checker(choose_instruction, choose_error, difficulty)
    if user_choice == "xxx":
        break


    def generate_easy_question():
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(['+', '-'])
        equation = f"{num1} {operator} {num2}"
        answer = eval(equation)
        return equation, answer


    def generate_medium_question():
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        num3 = random.randint(1, 20)
        operator1 = random.choice(['+', '-'])
        operator2 = random.choice(['+', '-'])
        equation = f"{num1} {operator1} {num2} {operator2} {num3}"
        answer = eval(equation)
        return equation, answer


    def generate_hard_question():
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        num3 = random.randint(1, 20)
        operator1 = random.choice(['+', '-', '*', '/'])
        operator2 = random.choice(['+', '-', '*', '/'])
        equation = f"{num1} {operator1} {num2} {operator2} {num3}"
        answer = eval(equation)
        return equation, answer


    def main():
        mode = input("Choose the mode (easy, medium, hard): ")
        if mode == "easy":
            equation, answer = generate_easy_question()
        elif mode == "medium":
            equation, answer = generate_medium_question()
        elif mode == "hard":
            equation, answer = generate_hard_question()
        else:
            print("Invalid mode selected!")
            return

        print("Math question:", equation)
        user_answer = float(input("Enter your answer: "))

        if user_answer == answer:
            print("Correct answer!")
        else:
            print("Incorrect answer!")
        if __name__ == "__main__":
            main()


    guess = int_check("Guess (or 'xxx' to exit): ")
    print("you guessed", guess)

    # compare guess to secret number

    if guess == secret:
        questions_won += 1
        break

    # check if we are out of rounds
    if questions_played >= questions:
        break

game_summary = []

questions_played = 5

questions_won = questions_played - questions_lost

# **** Calculate Game Stats
percent_win = questions_won / questions_played * 100
percent_lose = questions_lost / questions_played * 100

print()
print("***** Game History *****")
for game in game_summary:
    print(game)

print()

# displays game stats with : values to the nearest whole number
print("******* Game Statistics *******")
print("win: {}, ({:.0f}%)\nLoss: {}, "
      "({:.0f}%)".format(questions_won,
                         percent_win,
                         questions_lost,
                         percent_lose, ))
