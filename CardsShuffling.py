import random

variety = ["diamond","heart","spades","clubs"]
cards = ["ace","king","queen","jack","1","2","3","4","5","6","7","8","9","10"]

deck = []
for i in variety:
    for j in cards:
        deck.append(j + " of " + i)
random.shuffle(deck)

for k in deck:
    print(k)
