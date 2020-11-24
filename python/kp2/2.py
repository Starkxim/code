def main():
    global items
    fl1 = open("2.txt", 'r')
    wordCounts = {}
    count = 10
    for line in fl1:
        lineprocess(line.lower(), wordCounts)
        items0 = list(wordCounts.items())
        items = [[x, y] for (y, x) in items0]
        items.sort()

    for i in range(len(items) - 1, len(items) - count - 1, -1):
        print(items[i][1] + "\t" + str(items[i][0]))


def lineprocess(line, wordCounts):
    for ch in line:
        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line = line.replace(ch, "")
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1


main()
