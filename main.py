# Developer: H4ReMiiXxYT
# Permitted to edit this code to your will
# simple email generator
# :)
import os
import time
import random
import string
import json

nums = ["1","2","3","4","5","6","7","8","9","0",]
ran_chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v"]
tld = ["@yahoo.com", "@outlook.com", "@yopmail.com", "@gmail.com"]
msg_1 = input("""
Python Email Generator Made By H4ReMiiXxYT#6685

Press Any key to continue: 
""")
time.sleep(2)
os.system("clear") # if running on windows change this to cls
names = json.loads(open('unames.json').read()) # file names to read from
# Main Generator Function to be called
def generator():
    while True:
        random_email = random.choice(names) + random.choice(ran_chars) + random.choice(nums) + random.choice(tld)
        print("Email: " + random_email)

generator()