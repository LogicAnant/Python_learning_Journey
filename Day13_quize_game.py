import random

def main():
    while True:
        data = [
        ("Ques - how many colors in our flag?", "3"),
        ("Ques - what is the Chemical formula of Salt?","nacl"),
        ("Ques - how many bones in human body?","256"),
        ("how many contries in our world?","256"),
        ("how many minutes in one day?","1440")
        ]
        item = random.choice(data)
        questions = item[0]
        correct_answer = item[1]
        user_answer = input(questions)
        if user_answer.strip().lower() == correct_answer.lower().strip():
            print("congractulations you win 5 crore")
            break
        else:
            print("wrong answer please try again")
main()



