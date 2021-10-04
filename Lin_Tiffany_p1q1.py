# Quiz Creation Activity

import time
from rich import print



# Quiz has five questions the user will answer.
# It will keep track of score and give
# a final result
a = float(input(f"1 + 1 = "))
score = 0
if a == 2:
    print(f"You're right")
    score = score + 1
else:
    print(f"You're wrong")
b = input(f"Potter last name = ")
if b == 'Harry':
    print(f"You're right")
    score += 1
else:
    print(f"You're wrong")
c = input(f"Which of these choices are correct?")
if c == 'A':
    print(f"You're right")
    score = score + 1
else:
    print(f"You're wrong")
d = input(f"Who's the president of the United States?")
if d == 'Biden':
    print(f"You're right")
    score = score + 1
else:
    print(f"You're wrong")
e = float(input(f"4 / 2 = "))
if e == 2:
    print("You're right")
    score = score + 1
else:
    print("You're wrong")
if score == 5:
    print("Perfect!You're all right")
elif score == 4:
    print("Great!Only one mistake")
elif score == 3:
    print("Good!Just to mistakes")
elif score == 2:
    print("Well done!You get two right")
elif score == 1:
    print("Awesome!You get one right")
else:
    print("Come on...You need to prepare more")


questions = [
    ["What is the colour of the [bold italic red]sun[/bold italic red]?","yellow"]
]

# For each question, print it out and ask the user to answer
for question in questions:
    print(question[0])

    # Get the user's name
    user_answer = input ().lower().strip(",..?!")

    # See if they're correct
    if user_answer == question[1]:
        print("You got it right!")
    else:
        print("Sowwwwwie...You dead")



