
def revers_words(word):
    wor = []
    for i in word:
        wor.append(i[::-1])
    return wor


words = ["ABC","EFG","IJK","LMNOP"]
print(revers_words(words))