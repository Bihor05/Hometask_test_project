name = input("My name is: ")
spec = input("My speciality is: ")
math = int(input("My math score: "))
lang = int(input("My lang score: "))
prog = int(input("My prog score: "))
hist = int(input("My hist score: "))
score = float((math + lang + prog + hist)/4)
if 90 <= score <= 100:
    print(f"Wow! {name}, you pass exam. You have highest score: {score}.Its A mark! Well done!")
elif 75 <= score <= 89:
    print(f"Great! {name}, you pass exam. But you have middle score: {score}.Its B mark!")
elif 60 <= score <= 74:
    print(f"Done! {name}, you pass exam. But you have lowest score: {score}.Its C mark!")
elif score < 59:
    print(f"{name}, you failed your exam  Your score is {score}")

