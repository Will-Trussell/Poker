import random

class CardDeck:
    def __init__(self):
        self.deck = [""] * 52
        self.initializeDeck()
        self.shuffle()

    def initializeDeck(self):
        """ Initializes the deck to A -> K of Spades, Hearts, Clubs, Diamonds, in that order """
        suits = ["S", "H", "C", "D"]
        faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        i = 0
        for suit in suits:
            for face in faces:
                self.deck[i] = face + " " + suit
                i += 1

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, numPlayers=2):
        """ Deals two cards to the number of players specified (optional). 
        Default is 2 players. Max is 10. """
        if numPlayers > 10:
            raise Exception("Too many players! Max is 10.")
        hands = []
        i = 0
        for p in range(numPlayers):
            hands.append((self.deck[i], self.deck[i+1]))
            i += 2
        return hands


if __name__ == "__main__":
    deck = CardDeck()

    playerHands = deck.deal(numPlayers=10)
    for i in range(10):
        print(playerHands[i])
    