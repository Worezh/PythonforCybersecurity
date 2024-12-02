#!/usr/bin/env python3
# Typewriter simulator
# 
# By Sak

import random
import time

def type_sentence(sentence, error_rate=0.01):
  typed_sentence = ""
  for char in sentence:
    delay = random.uniform(0.1, 0.3)
    time.sleep(delay)  # Simulate typing speed
    # Introduce a typo with a probability of error_rate
    if random.random() < error_rate:
      # typo = chr(random.randint(97, 122))  # Random lowercase letter
      typo = random.choice([' ', '\t', chr(random.randint(97, 122)), chr(random.randint(65, 90))])
      typed_sentence += typo
    else:
      typed_sentence += char
    print(typed_sentence, end='\r')
  # Print a new line after each sentence
  print()

sentence = "All work and no play makes Jack a dull boy. "
while True:
    type_sentence(sentence)