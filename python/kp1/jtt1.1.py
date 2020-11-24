import collections
word=input()
word_mostcommon=collections.Counter(word).most_common(1)
print(word_mostcommon)