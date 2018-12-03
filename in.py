"""Getting Started Example for Python 2.7+/3.3+"""
text_a = open("a1.txt").read()
text_b = open("a1.txt").read()


text_c = open("a2.txt").read()
text_d = open("input1.txt").read()

text_1 = open("input1.txt").read()
text_2 = open("input1.txt").read()



say_a = open("data.txt").read()
say_b = open("data2.txt").read()
intro = open("intro.txt").read()
end = open("end.txt").read()

import nltk
import re
import os
import markovify
import time
import subprocess
import itertools
import requests
import json
import time, vlc
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

from os import system



class SentencesByChar(markovify.Text):
    def word_split(self, sentence):
        return list(sentence)
    def word_join(self, words):
        return "".join(words)


import random




session = Session(profile_name="winpython3")
polly = session.client("polly")



level = "word"
order = 3
order2 = 3

output_n = 1
weights = [0.8, 0.2]
weights2 = [0.8, 0.2]

length_limit = 400

names = ("Matthew", "Brian")
name = random.choice(names)
# name = "Brian"
print(name)

try:
    response = polly.synthesize_speech(Text= say_a+"my name is"+name+(intro)+say_b, OutputFormat="mp3",
                                        TextType="ssml", VoiceId=name)
except (BotoCoreError, ClientError) as error:
    print(error)
    sys.exit(-1)

if "AudioStream" in response:
    with closing(response["AudioStream"]) as stream:
        output = os.path.join(gettempdir(), "speech.mp3")

        try:
            with open(output, "wb") as file:
                file.write(stream.read())
        except IOError as error:
            print(error)
            sys.exit(-1)

else:
    print("Could not stream audio")
    sys.exit(-1)

if sys.platform == "win32":
    os.startfile(output)
else:
    subprocess.call(["afplay", output])

time.sleep(0.5)


for _ in itertools.repeat(None, 1):
    model_cls = markovify.Text if level == "word" else SentencesByChar
    gen_a = model_cls(text_a, state_size=5)
    gen_b = model_cls(text_b, state_size=5)
    gen_combo = markovify.combine([gen_a, gen_b], weights)
    counter=0
    for i in range(output_n):
        out = gen_combo.make_short_sentence(length_limit, test_output=False)
        out = out.replace("\n", "<break/>")
        out = out.replace(",", "<break/>")

        try:
            response = polly.synthesize_speech(Text= say_a+(out.lower())+say_b, OutputFormat="mp3",
                                                TextType="ssml", VoiceId=name)
        except (BotoCoreError, ClientError) as error:
            print(error)
            sys.exit(-1)

        if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:
                output = os.path.join(gettempdir(), "speech.mp3")

                try:
                    with open(output, "wb") as file:
                        file.write(stream.read())
                        print(out)
                        print()
                except IOError as error:
                    print(error)
                    sys.exit(-1)

        else:
            print("Could not stream audio")
            sys.exit(-1)

        if sys.platform == "win32":
            os.startfile(output)
        else:
            subprocess.call(["afplay", output])

time.sleep(0.3)


for _ in itertools.repeat(None, 1):
    model_cls = markovify.Text if level == "word" else SentencesByChar
    gen_c = model_cls(text_c, state_size=4)
    gen_d = model_cls(text_d, state_size=4)
    gen_combo = markovify.combine([gen_c, gen_d], weights2)
    counter=0
    for i in range(output_n):
        out = gen_combo.make_short_sentence(length_limit, test_output=False)
        out = out.replace("\n", "<break/>")
        out = out.replace(",", "<break/>")
        out = out.replace(".", "<break/>")
        # WORDS = ("Ivy", "Joanna", "Kendra", "Kimberly", "Salli", "Raveena", "Nicole", "Amy", "Emma", "Joey", "Justin", "Matthew", "Brian", "Geraint")
        # word = random.choice(WORDS)

        try:
            response = polly.synthesize_speech(Text= say_a+(out.lower())+say_b, OutputFormat="mp3",
                                                TextType="ssml", VoiceId=name)
        except (BotoCoreError, ClientError) as error:
            print(error)
            sys.exit(-1)

        if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:
                output = os.path.join(gettempdir(), "speech.mp3")

                try:
                    with open(output, "wb") as file:
                        file.write(stream.read())
                        print(out)
                        print()
                except IOError as error:
                    print(error)
                    sys.exit(-1)

        else:
            print("Could not stream audio")
            sys.exit(-1)

        if sys.platform == "win32":
            os.startfile(output)
        else:
            subprocess.call(["afplay", output])

time.sleep(0.3)

for _ in itertools.repeat(None, 10):
    model_cls = markovify.Text if level == "word" else SentencesByChar
    gen_c = model_cls(text_1, state_size=order2)
    gen_d = model_cls(text_2, state_size=order2)
    gen_combo = markovify.combine([gen_c, gen_d], weights2)
    counter=0
    for i in range(output_n):
        out = gen_combo.make_short_sentence(length_limit, test_output=False)
        out = out.replace("\n", "<break/>")
        out = out.replace(",", "<break/>")
        out = out.replace(".", "<break/>")

        # WORDS = ("Ivy", "Joanna", "Kendra", "Kimberly", "Salli", "Raveena", "Nicole", "Amy", "Emma", "Joey", "Justin", "Matthew", "Brian", "Geraint")
        # word = random.choice(WORDS)

        try:
            response = polly.synthesize_speech(Text= say_a+(out.lower())+say_b, OutputFormat="mp3",
                                                TextType="ssml", VoiceId=name)
        except (BotoCoreError, ClientError) as error:
            print(error)
            sys.exit(-1)

        if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:
                output = os.path.join(gettempdir(), "speech.mp3")

                try:
                    with open(output, "wb") as file:
                        file.write(stream.read())
                        print(out)
                        print()
                except IOError as error:
                    print(error)
                    sys.exit(-1)

        else:
            print("Could not stream audio")
            sys.exit(-1)

        if sys.platform == "win32":
            os.startfile(output)
        else:
            subprocess.call(["afplay", output])


time.sleep(0.7)
for _ in itertools.repeat(None, 1):
    model_cls = markovify.Text if level == "word" else SentencesByChar
    gen_a = model_cls(end, state_size=10)
    counter=0
    for i in range(output_n):
        out = gen_a.make_short_sentence(length_limit, test_output=False)
        out = out.replace("\n", "<break/>")
        out = out.replace(",", "<break/>")

        try:
            response = polly.synthesize_speech(Text= say_a+(out.lower())+say_b, OutputFormat="mp3",
                                                TextType="ssml", VoiceId=name)
        except (BotoCoreError, ClientError) as error:
            print(error)
            sys.exit(-1)

        if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:
                output = os.path.join(gettempdir(), "speech.mp3")

                try:
                    with open(output, "wb") as file:
                        file.write(stream.read())
                        print(out)
                        print()
                except IOError as error:
                    print(error)
                    sys.exit(-1)

        else:
            print("Could not stream audio")
            sys.exit(-1)

        if sys.platform == "win32":
            os.startfile(output)
        else:
            subprocess.call(["afplay", output])

time.sleep(0.3)

