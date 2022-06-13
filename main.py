
import random

while True:

    print('Lets play Rock Paper Scissors!\n\t Enter\n\t  "R" = Rock\n\t  "P" = Paper\n\t  "S" = Scissors')

    R = "R"
    P = "P"
    S = "S"
    all_choices = [R, P, S]

    user = input(f"Enter a choice ({R}, {P}, {S}): ").upper()

    if user not in all_choices:
        print("Invalid choice")


    computer = random.choice(all_choices)

    print(f"User chose {user}, computer chose {computer}")

    # r>s, p>r, s>p

    if user == computer:
        print("Tie")
    elif (user == R and computer == S) or (user == P and computer == R) or (user == S and computer == P):
        print("You won!")
        break
    else:
        print("You lost")
        break


