"""Getting Started Example for Python 2.7+/3.3+"""
text_a = open("input1.txt").read()
text_b = open("input2.txt").read()
text_c = open("input3.txt").read()

say_a = open("data.txt").read()
say_b = open("data2.txt").read()
intro = open("intro.txt").read()

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




# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).
session = Session(profile_name="winpython3")
polly = session.client("polly")



# change to "word" for a word-level model
level = "word"
# controls the length of the n-gram
order = 5
# controls the number of lines to output
output_n = 20
# weights between the models; text A first, text B second.
# if you want to completely exclude one model, set its corresponding value to 0
weights = [0.3, 0.3, 0.4]
# limit sentence output to this number of characters
length_limit = 1000

names = ("Ivy", "Joanna", "Kendra", "Kimberly", "Salli", "Raveena", "Nicole", "Amy", "Emma", "Joey", "Justin", "Matthew", "Brian", "Geraint")
name = random.choice(names)
print(name)

try:
    # Request speech synthesis
    response = polly.synthesize_speech(Text= say_a+(intro)+say_b, OutputFormat="mp3",
                                        TextType="ssml", VoiceId="Brian")
except (BotoCoreError, ClientError) as error:
    # The service returned an error, exit gracefully
    print(error)
    sys.exit(-1)

# Access the audio stream from the response
if "AudioStream" in response:
    # Note: Closing the stream is important as the service throttles on the
    # number of parallel connections. Here we are using contextlib.closing to
    # ensure the close method of the stream object will be called automatically
    # at the end of the with statement's scope.
    with closing(response["AudioStream"]) as stream:
        output = os.path.join(gettempdir(), "speech.mp3")

        try:
            # Open a file for writing the output as a binary stream
            with open(output, "wb") as file:
                file.write(stream.read())
        except IOError as error:
            # Could not write to file, exit gracefully
            print(error)
            sys.exit(-1)

else:
    # The response didn't contain audio data, exit gracefully
    print("Could not stream audio")
    sys.exit(-1)

# Play the audio using the platform's default player
if sys.platform == "win32":
    os.startfile(output)
else:
    subprocess.call(["afplay", output])




for _ in itertools.repeat(None, 50):
    model_cls = markovify.Text if level == "word" else SentencesByChar
    gen_a = model_cls(text_a, state_size=order)
    gen_b = model_cls(text_b, state_size=order)
    gen_c = model_cls(text_c, state_size=order)
    gen_combo = markovify.combine([gen_a, gen_b, gen_c], weights)
    counter=0
    for i in range(output_n):
        out = gen_combo.make_short_sentence(length_limit, test_output=False)

        # WORDS = ("Ivy", "Joanna", "Kendra", "Kimberly", "Salli", "Raveena", "Nicole", "Amy", "Emma", "Joey", "Justin", "Matthew", "Brian", "Geraint")
        # word = random.choice(WORDS)

        try:
            # Request speech synthesis
            response = polly.synthesize_speech(Text= say_a+(out.lower())+say_b, OutputFormat="mp3",
                                                TextType="ssml", VoiceId="Brian")
        except (BotoCoreError, ClientError) as error:
            # The service returned an error, exit gracefully
            print(error)
            sys.exit(-1)

        # Access the audio stream from the response
        if "AudioStream" in response:
            # Note: Closing the stream is important as the service throttles on the
            # number of parallel connections. Here we are using contextlib.closing to
            # ensure the close method of the stream object will be called automatically
            # at the end of the with statement's scope.
            with closing(response["AudioStream"]) as stream:
                output = os.path.join(gettempdir(), "speech.mp3")

                try:
                    # Open a file for writing the output as a binary stream
                    with open(output, "wb") as file:
                        file.write(stream.read())
                        print(out)
                        print()
                except IOError as error:
                    # Could not write to file, exit gracefully
                    print(error)
                    sys.exit(-1)

        else:
            # The response didn't contain audio data, exit gracefully
            print("Could not stream audio")
            sys.exit(-1)

        # Play the audio using the platform's default player
        if sys.platform == "win32":
            os.startfile(output)
        else:
            subprocess.call(["afplay", output])

try:
    # Request speech synthesis
    response = polly.synthesize_speech(Text= "Tell me what you think it was nothing and just my imagination." OutputFormat="mp3",
                                        TextType="ssml", VoiceId="Brian")
except (BotoCoreError, ClientError) as error:
    # The service returned an error, exit gracefully
    print(error)
    sys.exit(-1)
