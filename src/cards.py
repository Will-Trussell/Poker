class Card:
    def __init__(self, val, s):
        self.value = val
        self.suit = s
    def get_value(self):
        return self.value
    def set_value(self, val):
        self.value = val
    def get_suit(self):
        return self.suit
    def set_suit(self, s):
        self.suit = s
        