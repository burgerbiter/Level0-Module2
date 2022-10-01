import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    ask = simpledialog.askstring(title="question",prompt="Question")
    # Make a variable and initialize it to a random number between 0 and 3
    ball = random.randint(0,3)
    # If the random number is 0
    if ball == 0:
        print("Yes")
        # tell the user "Yes"

    # If the random number is 1
    elif ball == 1:
        print("No")
        # tell the user "No"

    # If the random number is 2
    elif ball == 2:
        print("Maybe you should ask Google?")
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    elif ball == 3:
        print("Please hold")
        # write your own answer
