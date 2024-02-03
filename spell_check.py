import textblob
import json
sentence = ['inconsistn teqnique', 'rugh estimite']
word_list = []
for item in sentence:
    word_list.append("")
    for char in item:
        if (ord(char) > 64 and ord(char) < 91) or (ord(char) > 96 and ord(char) < 123):
            word_list[-1] = word_list[-1] + char
        else:
            word_list.append("")
    
textblob_objects = list()
incorrect_words = list()
for word in word_list:
    incorrect_words.append(word)
    textblob_objects.append(textblob.TextBlob(word))

data = {}
for i in range(len(textblob_objects)):
    data[incorrect_words[i]] = str(textblob_objects[i].correct())

with open('data.json', 'w') as f:
    json.dump(data, f)
