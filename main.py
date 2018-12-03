import os 
import time
import subprocess

try:
    while True:
        os.system('python in.py')
        time.sleep(8)
except KeyboardInterrupt:
    print('interrupted!')