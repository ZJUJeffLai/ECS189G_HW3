import nltk
nltk.download('brown')
import collections

wordCount = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))
wordTotal = collections.defaultdict(lambda: 0)

lexicon = set(open('wordlist', 'r').read().split(' \n')[:-1])
missingLex = set(open('wordlist', 'r').read().split(' \n')[:-1])

wordTag = nltk.corpus.brown.tagged_words()

for w, t in wordTag:
    wordTotal[w] += 1
    if w in missingLex:
        missingLex.remove(w)
    if w in lexicon:
        wordCount[w][t] += 1

for w in wordCount:
    for t in wordCount[w]:
        prob = wordCount[w][t]
        print (t, '->', w, prob)

for w in missingLex:
    print (w)

