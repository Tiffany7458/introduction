# Quiz Creation Activity

# Quiz has five questions the user will answer.
# It will keep track of score and give
# a final result
answer = float(input(f"1 + 1 = "))
score = 0
if answer == 2:
    print(f"You're right")
    score = score + 1
else:
    print(f"You're wrong")
bnswer = input(f"Potter last name = ")
if bnswer == 'Harry':
    print(f"You're right")
    score += 1
else:
    print(f"You're wrong")
cnswer = input(f"Which of these choices are correct?")
if cnswer == 'A':
    print(f"You're right")
    score = score + 1
else:
    print(f"You're wrong")
if score == 3:
    print("Perfect!You're all right")
elif score == 2:
    print("Good!Only one mistake")
elif score == 1:
    print("Well done")
else:
    print("Come on")
