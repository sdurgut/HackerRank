import math

docs = """I'd like an apple
          An apple a day keeps the doctor away
          Never compare an apple to an orange
          I prefer scikit-learn to orange"""

count = lambda word, doc: sum(w == word for w in doc.split())
inner = lambda a, b: [aa * bb for aa, bb in zip(a, b)]
dot = lambda a, b: sum(inner(a, b))

words = list(set(docs.split()))
tf = [[count(word, doc) for word in words] for doc in docs.split('\n')]
idf = [math.log(1./(sum(word in doc for doc in docs.split('\n')))) for word in words]
tfidf = [inner(t, idf) for t in tf]
cosines = [dot(tfidf[0], t) / math.sqrt(dot(tfidf[0], tfidf[0])) / math.sqrt(dot(t, t))
           for t in tfidf[1:]]

print(cosines)
# We start with the second document
print (cosines.index(max(cosines)) + 2)