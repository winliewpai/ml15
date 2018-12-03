text_a = open("input.txt").read()
text_b = open("input2.txt").read()

a_words = text_a.split()
b_words = text_b.split()

import random
print(random.sample(a_words, 10))



from collections import Counter
Counter(text_a).most_common(12)

from scipy.stats import chi2_contingency
def compare_counts(a_count, b_count, count_threshold=1):
    a_total = sum(a_count.values())
    b_total = sum(b_count.values())
    sigs = []
    for k, v in a_count.items():
        if v <= count_threshold:
            continue
        sigs.append(
            (k,
             chi2_contingency([[v, a_total], [b_count[k], b_total]], lambda_=0)[0],
             "a" if v > b_count[k] else "b"))
    sigs.sort(key=lambda x: x[1], reverse=True)
    return sigs
def count_report(a_count, b_count, n=10, glue=""):
    compared = compare_counts(a_count, b_count)
    print("most significant")
    print("----------------")
    for item in compared[:n]:
        print(glue.join(item[0]), " (text ", item[2], "")
    print()
    print("least significant")
    print("-----------------")
    for item in compared[-n:]:
        print(glue.join(item[0]), " (text ", item[2], "")

count_report(Counter(a_words), Counter(b_words), 15)


def ngrams_for_sequence(n, seq):
    return [tuple(seq[i:i+n]) for i in range(len(seq)-n+1)]


import random
a_9grams = ngrams_for_sequence(9, text_a)
print(random.sample(a_9grams, 10))

b_word_5grams = ngrams_for_sequence(5, text_b.split())
print(random.sample(b_word_5grams, 10))

from collections import Counter
a_count = Counter(ngrams_for_sequence(3, text_a.split()))
b_count = Counter(ngrams_for_sequence(3, text_b.split()))

a_count.most_common(12)

b_count.most_common(12)

count_report(a_count, b_count, 12, " ")



