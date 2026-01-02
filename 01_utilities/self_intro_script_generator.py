from datetime import datetime
question = [
    "What is your name? ",
    "What is your age ",
    "Where do you live? ",
    "What is your profession? ",
    "What is your hobbies? "
]

answer = []

for q in question:
    a = input(q).strip()
    answer.append(a)

intro_message = (
      f"""\nHello! My name is {answer[0]}. 
      I am {answer[1]} years old and live in {answer[2]}
      I work as a {answer[3]} 
      and I absolutely enjoy {answer[4]} in my free 
      time. Nice to meet you!\n""")
current_date = datetime.now()

border = "*"*80
print(border, intro_message, current_date, border)

