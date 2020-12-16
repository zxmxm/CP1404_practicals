word_count = {}
text = input("Text:")

words = text.split()
for word in words:
    f = word_count.get(word, 0)
    word_count[word] = f + 1

words = list(word_count.keys())

for word in words:
    print("{} : {}".format(word, word_count[word]))