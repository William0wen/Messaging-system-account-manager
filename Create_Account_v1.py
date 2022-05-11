"""Create account, or log into existing account"""


def yes_no(question, y_ans, n_ans):
    while True:
        answer = input(question).lower().strip()
        if answer == "yes" or answer == "y":
            return(y_ans)
            pass
        elif answer == "no" or answer == "n":
            return(n_ans)
            pass


print("*** WELCOME TO THE WOMAS MESSAGING SYSTEM ***")

print(yes_no("do you like this system? ", "Good", "Not good"))

