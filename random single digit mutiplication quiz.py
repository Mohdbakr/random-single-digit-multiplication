import random
from threading import Timer
import threading
from time import *

def countdown():
    global timer
    timer = 60

    for x in range(60):
        timer = timer - 1
        sleep(1)
    print("Time is ended")

def random_multiply():

    points = 0
    questions = 0
    countdown_thread = threading.Thread(target =countdown)
    countdown_thread.start()
    while timer >0:
        x= random.randint(0,9)
        y = random.randint(0,9)
        print(f"what is {x} X {y} = ")
        answer = input("")
        questions += 1
        if answer =="" or int(answer) != (x*y):
            print(f"Incorrect. The answer is {str(x*y)}.")
        else:
            print("Correct!")
            points += 1
            
    print(f"Time is up.\nYour score is {points} of {questions}")
    sleep(10)

random_multiply()