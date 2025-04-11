import random
import time
from termcolor import colored
print('''
.##....##..#######..##.....##.....######..########.########.##....##.......###....##....##..######..##......##.########.########...######...#######.
..##..##..##.....##.##.....##....##....##.##.......##.......##...##.......##.##...###...##.##....##.##..##..##.##.......##.....##.##....##.##.....##
...####...##.....##.##.....##....##.......##.......##.......##..##.......##...##..####..##.##.......##..##..##.##.......##.....##.##.............##.
....##....##.....##.##.....##.....######..######...######...#####.......##.....##.##.##.##..######..##..##..##.######...########...######......###..
....##....##.....##.##.....##..........##.##.......##.......##..##......#########.##..####.......##.##..##..##.##.......##...##.........##....##....
....##....##.....##.##.....##....##....##.##.......##.......##...##.....##.....##.##...###.##....##.##..##..##.##.......##....##..##....##..........
....##.....#######...#######......######..########.########.##....##....##.....##.##....##..######...###..###..########.##.....##..######.....##....''')
#prompt for user to enter their name
while True:
    name=input("Input your name (or type exit to quit): ")
    if name == "exit":
        print("Fool!")
        quit()
    elif name == "":
        print("You must have and enter a name\n If you have forgotten your name you are beyond my help")
        continue
    else:
        break

#while loop to validate question asked
while True:
#prompt for user to ask question
    question = input("What is your Yes or No question?: ")
    coloured_question=colored(question, "red", "on_white", attrs=["blink","underline","reverse"] )
#input validation of question
    if question  == "":
        print("Do not mock the fates and ask them a question!")
        continue
    if name == "" and question == "":
        print("You are a fool of a nameless agentless being!")
        quit()
    else:
        print("|{}|".format("-" * 40))
        print(name+" Your question is:\n |{}|\nThe fates shall decide!".format(coloured_question))
        print("|{}|".format("-" * 40))
        break
#defining a function to generate answer
def generate_answer():
    answer=""
    random_number = random.randint(1,10)
    if random_number == 1:
        answer += "Yes - definitely"
    elif random_number == 2:
        answer += "It is decidedly so"
    elif random_number == 3:
        answer += "Without a doubt"
    elif random_number == 4:
        answer += "Reply hazy, try again"
    elif random_number == 5:
        answer += "Ask again later"
    elif random_number == 6:
        answer += "You do not deserve this answer"
    elif random_number == 7:
        answer += "My sources say no"
    elif random_number == 8:
        answer += "Outlook not so good"
    elif random_number == 9:
        answer += "Very doubtful"
    elif random_number == 10:
        answer += "Only the gods can help you there."
    else:
        print("Error")
    print(name+" Your fate has been decided\n\n The answer you seek is: ")
    time.sleep(1)
    coloured_answer = colored(answer, "white", "on_green", attrs=["blink"])
    print("+{}+".format("-" * (len(coloured_answer) - 2)))
    print("|{}|".format(coloured_answer))
    print("+{}+".format("-" * (len(coloured_answer) - 2)))
#Sleep to make it feel like theres processing time
time.sleep(3)
#generate the answer
if name != "" and question != "":
    generate_answer()
#while loop to check for any additonal questions. 
time.sleep(2)
while True:
    print("Do you require more answers?")
    question=input("What is your question? (type 'exit' to quit): ")
    if question == "exit":
        quit()
    elif question == "":
        continue
    else:
        generate_answer()

    