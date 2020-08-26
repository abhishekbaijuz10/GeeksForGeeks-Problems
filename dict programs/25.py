from collections import Counter

Dict = ["go", "bat", "me", "eat", "goal", "boy", "run",]
arr = ['e', 'o', 'b', 'a', 'm', 'g', 'l']


def char_check(word):
    temp = 1
    sample = Counter(word)
    for key in sample.keys():
        if key not in arr:
            temp = 0
            return temp


def main():
    for word in Dict:
        word_collect = char_check(word)
        if word_collect != 0:
            print(word)


main()
