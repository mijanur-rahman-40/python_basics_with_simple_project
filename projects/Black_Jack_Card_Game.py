import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.rank


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has :' + deck_comp

    def shuffle(self):
        # here shuffle method change the order of the list
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def addCard(self, card):
        # card passed in
        # from deck.deal()
        self.cards.append(card)
        self.value += values[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjustForAce(self):
        # if total value >21 and I still have an ace
        # than change my ace to be a i instead of an 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, total=100):
        # This can be set to a default value or supplied by a user input
        self.total = total
        self.bet = 0

    def winBet(self):
        self.total += self.bet

    def loseBet(self):
        self.total -= self.bet


def takeBet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet : '))
        except:
            print('Sorry, a bet must be an integer')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed! You have: {}".format(chips.total))
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.addCard(single_card)
    hand.adjustForAce()


def hitOrStand(deck, hand):
    global playing
    while True:
        x = input('Hit or Stand? Enter h or s : ')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player Students Dealer's Turn")
            playing = False
        else:
            print('Sorry, I did not understand that,Please enter h or s only!')
            continue
        break


def showSome(player, dealer):
    print("Dealer's Hand:")
    print("one card hidden!")
    print('', dealer.cards[1])
    print('\n')
    print("Player's Hand:")
    for card in player.cards:
        print(card)


def showAll(player, dealer):
    print("Dealer's Hand: ")
    for card in dealer.cards:
        print(card)
    print('\n')
    print("Player's Hand: ")
    for card in player.cards:
        print(card)


def playerBusts(player, dealer, chips):
    print('BUST player')
    chips.loseBet()


def playerWins(player, dealer, chips):
    print('Player wins')
    chips.winBet()


def dealerBusts(player, dealer, chips):
    print('Player wins! dealer busted')
    chips.winBet()


def dealerWins(player, dealer, chips):
    print('Dealer wins')
    chips.loseBet()


def push(player, dealer):
    print('Dealer and player tie! PUSH')


while True:
    # Print an opening statement

    print('Welcome to blackjack')
    # create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.addCard(deck.deal())
    player_hand.addCard(deck.deal())

    dealer_hand = Hand()
    dealer_hand.addCard(deck.deal())
    dealer_hand.addCard(deck.deal())

    # set up the player chips
    player_chips = Chips()

    # Prompt the player for their bet
    takeBet(player_chips)

    # show cards (but keep one dealer card hidden)
    showSome(player_hand, dealer_hand)

    # recall this playing variable from our hitOrStand function
    while playing:

        # prompt for player to hit or stand
        hitOrStand(deck, player_hand)

        #  show cards (but keep one dealer card hidden)
        showSome(player_hand, dealer_hand)

        # if player's hand exceeds 21, run playerBusts() amd break out of loop
        if player_hand.value > 21:
            playerBusts(player_hand, dealer_hand, player_chips)
            break

        # if player has not busted, play dealer's hand until dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < player_hand.value:
                hit(deck, dealer_hand)

            # show al cards
            showAll(player_hand, dealer_hand)
            # run different winning scenarios
            if dealer_hand.value < 21:
                dealerBusts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealerWins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                playerWins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

    # inform player of their chips total
    print('\n Player total chips are at : {}'.format(player_chips.total))
    # ask to play again
    new_game = input('Would you like to play another hand? y/n ')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Tank you for playing')
        break
