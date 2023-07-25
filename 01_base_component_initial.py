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


def check_rounds():
    while True:
        response = input("how many rounds: ")

        round_error = "Please type either <enter> " \
                      " or an integer that is more than 0\n"
        # If infinite
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
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
questions: int = 0
questions_played = 0
questions_won = 0
questions_lost = 0

# rounds loop
end_game = "no"

if questions == "":
    heading = "infinite" \
              'question {}'.format(questions_played + 1)
else:
    heading = "questions {} of " \
              "{}".format(questions_played + 1, questions)

    while True:
        num_1 = random.randint(1, 20)
        num_2 = random.randint(1, 20)
        num_3 = random.randint(1, 20)
        num_4 = random.randint(1, 20)

        easy = f"{num_1} + {num_2} - {num_3}"
        medium = f"{num_1} * {num_2} + {num_3}"
        hard = f"{num_1} *  {num_2} / {num_3} + {num_4}"

        answer_1 = num_1 + num_2 - num_3
        answer_2 = num_1 * num_2 + num_3
        answer_3 = num_1 * num_2 / num_3 + num_4

        print("question:", easy, medium, hard)
        print("answer:", answer_1, answer_2, answer_3)
        mode_list = [easy, medium, hard, xxx]

        print("please choose a mode between easy/medium/hard")
        choose_instruction = "Please choose easy (e), medium " \
                             "(m) or hard (h)" \
                             "or 'xxx' to exit: "
        choose_error = "Please choose from easy / " \
                       "medium / hard (or xxx to quit)"

        user_choice = [choose_instruction, choose_error, mode_list]
        if user_choice == "xxx":
            break
    print("Start Guessing!!")
    print()
    guess = int_check("Guess (or 'xxx' to exit): ")
    print("you guessed", guess)


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
