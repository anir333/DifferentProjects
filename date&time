import datetime
option1 = "- If you want to know the date write as an answer (date)"
option2 = "- If you want to know the time write as an answer (time)"
option3 = "- If you want to know both write as an answer (both)"
to_stop = "If you want the program to stop write as an answer (quit)"
date = datetime.date.today()
from datetime import datetime
time = datetime.now().strftime("%H:%M:%S")

print(f"What do you want to know, the date or the time? ")
print(option1)
print(option2)
print(option3)
print(to_stop)


while True:
    answer = input("Answer: ")
    if answer.lower() == "date":
        print(date)
    elif answer.lower() == "time":
        print(time)
    elif answer.lower() == "both":
        print(date, time)
    elif answer.lower() == "quit":
        break
    else:
        print(f"Incorrect answer, {option1, option2}")
