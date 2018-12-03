from textgenrnn import textgenrnn
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'
textgen = textgenrnn()
textgen.train_from_file('input1.txt', num_epochs=5)
textgen.generate(5)