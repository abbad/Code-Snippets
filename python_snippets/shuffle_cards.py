from random import randint

def shuffle(cards):
    cards_len = len(cards) - 1
    while cards_len > 0:
        i = randint(0, cards_len)
        temp = cards[cards_len]
        cards[cards_len] = cards[i]
        cards[i] = temp
        cards_len -= 1
    print(cards)


if __name__ == '__main__':
    cards = []
    for x in range(0, 52):
        cards.append(x)

    shuffle(cards)