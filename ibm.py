from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1


text_to_speech = TextToSpeechV1(
    iam_apikey='sz6H8LevNTGD8wn8_fBqFZ61lrUDtuHAFwuD1TFaguPr',
    url='https://gateway-wdc.watsonplatform.net/text-to-speech/api'
)

response = text_to_speech.synthesize(
        'Hello world!')