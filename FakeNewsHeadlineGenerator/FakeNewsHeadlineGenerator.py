#import random Function to random choices
import random

#Create the Lists
names = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Sita raman",
    "Rahul Gandi",
    "Monkey",
    "The Street Dogs",
    "The Corporate Employee"
]

actions =[
    "playing crick",
    "acting fabulous",
    "Dancing ",
    "Speaking truth",
    "running to fast",
    "working hard for money"
]

places =[
    "in Bengaluru",
    "at Stage",
    "in Streets",
    "in Company",
    "infront of indra canteen",
]

#while loop for continues headline generating
while True:
    name = random.choice(names)
    action = random.choice(actions)
    place = random.choice(places)
    print(f'Breaking News: {name} {action} {place}')

    user_input= input("\n you want more NEWS: (yes/no):").strip().lower()
    if user_input == "no":
        break

print("Have a nice day!\n thank you")





