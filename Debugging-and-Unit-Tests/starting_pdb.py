import string
text = "This is a test sentence used as our text corpus, which is what makes this text generator work."

bigrams = {}

# Remove punctuation from sentences
for char in string.punctuation:
    text = text.replace(char, '')
# Split by word
words = text.split()
import pdb; pdb.set_trace()
for i in range(len(words)):
    # Add empty list to dict if none there
    if words[i] not in bigrams:
        bigrams[words[i]] = []
    # Add bigram to dict
    bigrams[words[i]].append(words[i+1])

bigrams
