import random

cards = [x for x in range (1,53)]
print ("Unshuffled deck of cards")
print ("========================")
print(cards)
print ("\n")

for i in range(0,1000000) :
    card1 = random.randint(0,51)
    # print(f"card 1: {card1}")
    card2 = random.randint(0,51)
    # print(f"card 2: {card2}")
    cards[card1], cards[card2] = cards[card2], cards[card1]

print ("Your cards have been shuffled")
print ("=============================\n")
print (cards)
