import os
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

lines = [
    ("My chest is hurting", 0.10),
    ("My feet can't fall out of bed", 0.08),
    ("I don't know where to go", 0.075), 
    ("So I'll lay here instead", 0.08),
    ("With my symptoms", 0.075),
    (", symptoms of sorrow and dread", 0.08),
    ("They all said it would fade, but again and again", 0.09),
    ("I loveeee", 0.11),
    ("I LOVEEEE", 0.15),
    ("I love, ", 0.085),
    ("I love, ", 0.085),
    ("I love", 0.085),
    ("I loveeee", 0.11),
    ("I LOVEEEEEEEE", 0.15),
    ("I LOVEEEEEEEE", 0.15),
]

delays = [0.45, 0.55, 0.5, 0.5, 0.85, 0.75, 0.85, 1.3, 0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 100]

clear()

def print_lyrics():
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(char_delay)
        time.sleep(delays[i])
        if (i==4 or i==9 or i==10):
            continue
        print()
        

print_lyrics()
