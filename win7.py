from tts_watson.TtsWatson import TtsWatson 

ttsWatson = TtsWatson('nliewpai@risd.edu', 'winRISD1', 'en-US_AllisonVoice') # en-US_AllisonVoice is a voice from watson you can found more to: https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/doc/text-to-speech/using.shtml#voices 
ttsWatson.play("The text which i want to be a sound") 