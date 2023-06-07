import random
import math


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
    print("***** How To Play *****")
    print()
    print("it's a math game")
    print("You should try and improve your maths skills. ")
    print()
    print("Have Fun :)")
    print()


def level():
    print("please choose a level from 1 - 4")
    print("1 being the easiest and 4 being the hardest")


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
                           "before? ")

rounds_played = 0
rounds_won = 0
low_number = int_check("Please choose a low number: ")
high_number = int_check("Please choose a high number: ", low_number)

var_range = high_number - low_number + 1
max_raw = math.log2(var_range)
max_upped = math.ceil(max_raw)
max_guesses = max_upped + 1

print("Max Guesses: {}".format(max_guesses))

mode = "regular"

rounds = int_check("How many rounds: ", 1, exit_code="")

if rounds == "":
    mode = "infinite"
    rounds = 5

# rounds loop
end_game = "no"
while rounds_played <= rounds:

    guesses_allowed = max_guesses

    while guesses_allowed <= max_guesses:

        if mode == "infinite":
            heading = f"Round {rounds_played + 1} (infinite mode)"
            rounds += 1
        else:
            heading = f"Round {rounds_played + 1} of {rounds}"

        print(heading)

        secret = random.randint(low_number, high_number)

        rounds_played += 1

        guesses_allowed = max_guesses

        print("Start Guessing!!")
        while True:

            guess = int_check("Guess (or 'xxx' to exit): ",
                              low_number, high_number, )
            print("you guessed", guess)

            if guess == "xxx":
                end_game = "yes"
                break

            # compare guess to secret number

            if guess == secret:
                rounds_won += 1
                break

        # check if we are out of rounds
        if rounds_played >= rounds:
            break
        if guesses_allowed <= 0:
            print("sorry you lose")
            break

game_summary = []

rounds_lost = 0
rounds_played = 5

rounds_won = rounds_played - rounds_lost

# **** Calculate Game Stats
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

print()
print("***** Game History *****")
for game in game_summary:
    print(game)

print()

# displays game stats with : values to the nearest whole number
print("******* Game Statistics *******")
print("win: {}, ({:.0f}%)\nLoss: {}, "
      "({:.0f}%)".format(rounds_won,
                         percent_win,
                         rounds_lost,
                         percent_lose, ))
