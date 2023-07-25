import random

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
