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


show_instructions = yes_no("Have you played this game before? ")
