#choice is a fuction or a member in the random module that is expecting a sequence 
from random import choice
enames=["Rahul", "Sonia", "Priya", "X", "Y", "Z", "Kiran", "Jay", "H", "I"]
for x in range(2):
    print(choice(enames))
