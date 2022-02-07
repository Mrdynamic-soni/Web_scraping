import re

def count(word):
    return len(re.findall('(?!e$)[aeiouy]+', word, re.I) +
               re.findall('^[^aeiouy]*e$', word, re.I))

file = open("new.txt","r")
words = file.read().split()
complex_word = []
for word in words:
    if count(word) >=2:
        complex_word.append(word)

print(complex_word)
print(len(complex_word))
print(len(words))

precentage_complex_word = len(complex_word)/len(words)
print(precentage_complex_word)