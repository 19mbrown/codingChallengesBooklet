from os import system


quesAndAns = dict()

while True:
    question = input("Enter a question: ")
    answer = input("What's the answer: ")
    quesAndAns[question] = answer
    if input("Do you want to add another ? (y/n) ") != "y":
        print("\033c", end="")
        break

for ques in quesAndAns.keys():
    print(ques)
    if input("Answer: ").lower != quesAndAns[ques].lower():
        print("Wrong answer :(")
        print(f"The correct answer is {quesAndAns[ques]}")
