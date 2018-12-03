import markovify
import nltk
import re

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence
        
corpus = open("input1.txt").read()

text_model = markovify.Text(corpus, state_size=3)
model_json = text_model.to_json()

reconstituted_model = markovify.Text.from_json(model_json)
reconstituted_model.make_short_sentence(140)