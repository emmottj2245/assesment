
def choice_checker(question, valid_list, error):
    while True:

        # Ask user for choice
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)


choose_instruction = "Please choose easy (e), medium " \
                     "(m), or hard (h), " \
                     "or 'xxx' to exit: "
choose_error = "Please choose from easy / " \
               "medium / hard (or xxx to quit)"

difficulty = ['easy', 'medium', 'hard', 'xxx']

while True:

    user_level = choice_checker(choose_instruction, difficulty, choose_error)
    print(user_level)
