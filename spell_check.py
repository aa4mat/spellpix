import textblob
sentence = ['inconsistn teqnique', 'rugh estimite']
textblob_objects = list()
for word in sentence:
    textblob_objects.append(textblob.TextBlob(word))


for textblob_object in textblob_objects:
    print(textblob_object.correct())