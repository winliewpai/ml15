filename = 'input2.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

words = text.split()


import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
print(stripped[:100])

