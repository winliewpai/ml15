text_a = open("input.txt").read()
text_b = open("input2.txt").read()

import os
import markovify
import time
import subprocess
import itertools
import requests
import json

from watson_developer_cloud import TextToSpeechV1

text_to_speech = TextToSpeechV1(
    iam_apikey='sz6H8LevNTGD8wn8_fBqFZ61lrUDtuHAFwuD1TFaguPr',
    url='https://gateway-wdc.watsonplatform.net/text-to-speech/api'
)
from tts_watson.TtsWatson import TtsWatson
tts = TtsWatson("**Username**", "**Password**", "en-US_Allisonvoice")
tts.play("Test")