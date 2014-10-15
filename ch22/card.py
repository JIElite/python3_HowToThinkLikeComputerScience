

class Card:
    suits = ( "Clubs", "Diamonds", "Hearts", "Spade" )
    ranks = ( "reserved", "Ace", "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "Jack", "Queen", "King")

    def __init__(self, suit = 0, rank = 0):
        import sys
        line = sys._getframe(1).f_lineno
        try:
            if suit > 3 or rank > 14:
                raise ValueError
            self.suit = suit
            self.rank = rank
        except ValueError:
            print("The ValueError occured in the line: {0}".format(line))

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    def cmp(self, other):
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1

        #the Rank is SAME
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        #Suit and Rank is Same , tight condition
        return 0

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0




if __name__ == "__main__":
    c1 = Card(1,11)
    c2 = Card(1,13)

    cards = [];
    cards.append(Card(1,12))
    print( c1 in cards )
    print( c2 in cards )
    print(cards)
