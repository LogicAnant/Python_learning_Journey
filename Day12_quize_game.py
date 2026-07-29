import random

def main():
    while True:
        data = [
            ("Ques - How many colors in our flag? ", "3"),
            ("Ques - What is the chemical formula of Salt? ", "nacl"),
            ("Ques - How many bones in a human body? ", "206"),
            ("Ques - How many countries in our world? ", "195"),
            ("Ques - How many minutes in one day? ", "1440")
        ]
        item = random.choice(data)
        question = item[0]
        correct_answer = item[1]
        user_answer = input(question
         if user_answer.strip().lower() == correct_answer.lower().strip():
            print("Congratulations! You win 5 crore 🎉\n")
            break
        else:
            print("Wrong answer! Please try again.\n")

if __name__ == "__main__":
    main()



