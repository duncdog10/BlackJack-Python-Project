import random
import time

decklist = [("Ace of Spades", 1), 	("Ace of Hearts", 1), 	("Ace of Clubs", 1), 	("Ace of Diamonds", 1), 	("Two of Spades", 2), 	("Two of Hearts", 2), 	("Two of Clubs", 2), 	("Two of Diamonds", 2), 	("Three of Spades", 3), 	("Three of Hearts", 3), 	("Three of Clubs", 3), 	("Three of Diamonds", 3), 	("Four of Spades", 4), 	("Four of Hearts", 4), 	("Four of Clubs", 4), 	("Four of Diamonds", 4), 	("Five of Spades", 5), 	("Five of Hearts", 5), 	("Five of Clubs", 5), 	("Five of Diamonds", 5), 	("Six of Spades", 6), 	("Six of Hearts", 6), 	("Six of Clubs", 6), 	("Six of Diamonds", 6), 	("Seven of Spades", 7), 	("Seven of Hearts", 7), 	("Seven of Clubs", 7), 	("Seven of Diamonds", 7), 	("Eight of Spades", 8), 	("Eight of Hearts", 8), 	("Eight of Clubs", 8), 	("Eight of Diamonds", 8), 	("Nine of Spades", 9), 	("Nine of Hearts", 9), 	("Nine of Clubs", 9), 	("Nine of Diamonds", 9), 	("Ten of Spades", 10), 	("Ten of Hearts", 10), 	("Ten of Clubs", 10), 	("Ten of Diamonds", 10), 	("Jack of Spades", 10), 	("Jack of Hearts", 10), 	("Jack of Clubs", 10), 	("Jack of Diamonds", 10), 	("Queen of Spades", 10), 	("Queen of Hearts", 10), 	("Queen of Clubs", 10), 	("Queen of Diamonds", 10), 	("King of Spades", 10), 	("King of Hearts", 10), 	("King of Clubs", 10), 	("King of Diamonds", 10)]
your_hand = []
your_total = 0
dealer_hand = []
dealer_total = 0
discard_pile = []

def hand_status ():
    print("Your hand:")
    print([cards[0] for cards in your_hand])
    print(f"Hand total: {sum([total[1] for total in your_hand])}")
    print(f"Dealer showing:{dealer_hand[0][0]}")
    dealer_faceup = dealer_hand[0][1]
    print(f"Dealer total: {dealer_faceup} + ???")



def restart():
    start_again = input("Play again? \n(y/n): ")
    while start_again != "y" and start_again != "n":
        start_again = input("Let's try that one more time. Play again? \n(y/n): ")
    if start_again == "y":
        start_game()
    elif start_again == "n":
        print("Thanks for playing!")

def add_card ():
    your_hand.append(random.choice(decklist))
    hand_status()
    if sum([total[1] for total in your_hand]) > 21:
        print("Bust! You Lose")
        discard_cards()
        restart()
    else:
        hit_or_stay()

def win_or_lose():
    print(f"Your hand: {[cards[0] for cards in your_hand]}")
    print(f"Your hand total: {sum([total[1] for total in your_hand])}")
    print(f"Dealer Hand: {[cards[0] for cards in dealer_hand]}")
    print(f"Dealer Total: {sum(total[1] for total in dealer_hand)}")
    time.sleep(1)
    while sum([total[1] for total in dealer_hand]) <= 16:
        dealer_new_card = random.choice(decklist)
        print(f"Dealer Hits: {dealer_new_card[0]}")
        dealer_hand.append(dealer_new_card)
        decklist.remove(dealer_new_card)
        print(f"Dealer total: {sum([total[1] for total in dealer_hand])}")
        time.sleep(1)
    if sum([total[1] for total in your_hand]) > sum([total[1] for total in dealer_hand]):
        print(f"Your total: {sum([total[1] for total in your_hand])}, Dealer total: {sum([total[1] for total in dealer_hand])}")
        time.sleep(1)
        print("-----------\n| You Win! |\n-----------")
    elif sum([total[1] for total in your_hand]) < sum([total[1] for total in dealer_hand]) and sum([total[1] for total in dealer_hand]) <= 21:
        print(f"Your total: {sum([total[1] for total in your_hand])}, Dealer total: {sum([total[1] for total in dealer_hand])}")
        time.sleep(1)
        print("------------\n| You Lose! |\n------------")
    elif sum([total[1] for total in dealer_hand]) > 21:
        print("------------------\n| Dealer Busts. |\n-----------\n| You win! |\n-----------")
    else:
        print(f"Your total: {sum([total[1] for total in your_hand])}, Dealer total: {sum([total[1] for total in dealer_hand])}")
        time.sleep(3)
        print("----------\n| Both hands are equal. |\n| Push! |\n----------")
    discard_cards()
    restart()


def discard_cards():
    while len(your_hand) > 0:
        for card in your_hand:
            if card in your_hand:
                your_hand.remove(card)
                discard_pile.append(card)
    while len(dealer_hand) > 0:
        for card in dealer_hand:
            if card in dealer_hand:
                dealer_hand.remove(card)
                discard_pile.append(card)
    print(f"Discard pile contains: {len(discard_pile)} cards")
    print(f"Cards remaining in deck: {len(decklist)} cards")

def hit_or_stay():
    hitstay = input("Hit or Stay? \n(h/s): ")
    while hitstay != "h" and hitstay != "s":
        hitstay = input("Let's try that again. Hit or stay? \n(h/s): ")
    if hitstay == "h":
        add_card()
    elif hitstay == "s":
        win_or_lose()

def deal_cards():
    while len(your_hand) < 2:
        your_hand.append(random.choice(decklist))
        for card in decklist:
            if card in your_hand:
                decklist.remove(card)
    while len(dealer_hand) <2:
        dealer_hand.append(random.choice(decklist))
        for card in decklist:
            if card in dealer_hand:
                decklist.remove(card)
    hand_status()
    hit_or_stay()

def shuffle_deck():
    while len(your_hand) > 0:
        decklist.append(your_hand)
        for card in your_hand:
            if card in decklist:
                your_hand.remove(card)
    while len(dealer_hand) > 0:
        decklist.append(dealer_hand)
        for card in dealer_hand:
            if card in decklist:
                dealer_hand.remove(card)
    print("Deck Shuffled")
    start_deal = input("Deal Cards? \n(y/n): ")
    while start_deal != "y" and start_deal != "n":
        start_deal = input("Let's try again. Deal Cards? \n(y/n):")
    if start_deal == "y":
        deal_cards()
    elif start_deal == "n":
        continue_prompt = input("Deal Cards? \n(y/n): ")



def start_game():
    start_shuffle = input("Shuffle deck? \n(y/n): ")
    while start_shuffle != "y" and start_shuffle != "n":
        start_shuffle = input("Let's try again. Shuffle deck? \n(y/n): ")
    if start_shuffle == "y":
        shuffle_deck()
    elif start_shuffle == "n":
        continue_prompt = input("Deal Cards? \n(y/n): ")
        while continue_prompt != "y":
            continue_prompt = input("Let's try again. Deal Cards? \n(y/n): ")
        if continue_prompt == "y":
            deal_cards()



print("Welcome to Blackjack!")
start_game()



#
#print("Your hand:")
#print([cards[0] for cards in your_hand])
#print("Hand total:")
#print(sum([total[1] for total in your_hand]))
#print("Dealer showing:")
#print(dealer_hand[0][0])
#print(decklist)