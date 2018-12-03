import os
import markovify
import time
import subprocess
import itertools

# Get raw text as string.
with open("input2.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)
def say(text):
    subprocess.call(['say', text])

# Print five randomly-generated sentences
for i in range(1):
    say(text_model.make_sentence())
    print(text_model.make_sentence())

