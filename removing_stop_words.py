#import required library to perfoem operation
import nltk
# nltk.download()
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

file = open("C:\\Users\\Acer\\Desktop\\black_coffer\\data.text","r+")
# word = file.read().split()
# print(len(file.read().split()))
# file_read =file.read()

stop_words = set(stopwords.words('english'))

token_words = word_tokenize(file.read())
print(len(token_words))
filtered_words = []

f =open("new_data.txt","a")

for word in token_words:
    if  not word.lower() in  stop_words:
        filtered_words.append(word)
        f.write(f"{word} ")
print(len(filtered_words))


