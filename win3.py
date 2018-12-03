text_a = open("input2.txt").read()

import random
import os
import markovify
import time
import subprocess
import itertools
from textgenrnn import textgenrnn

textgen = textgenrnn(name="text_a")
textgen.generate()

from markovify.splitters import split_into_sentences
text_a_sentences = split_into_sentences(text_a)




textgen = textgenrnn("text_a_weights.hdf5")

textgen.generate(10, temperature=0.1)
