import math


def paint_cal(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)  # math.celi is used to rounded up a number.
    print(f"You will need {num_of_cans} cans of paint.")


test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5
paint_cal(height=test_h, width=test_w, cover=coverage)

