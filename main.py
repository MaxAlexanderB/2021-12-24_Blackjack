from art import logo
import random

#------------- Lists and Dictionaries---------------#
cards_list = [
    "Ace",
    "King",
    "Queen",
    "Jack",
    "10",
    "9",
    "8",
    "7",
    "6"
]
cards_dictionary = {
    "Ace": 11,
    "King": 10,
    "Queen": 10,
    "Jack": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6
}

#------------- Variables: These are Global. to access global in function type global----------#

player = []
dealer = []


#------------- Functions:----------------#

def chose_card():  # can collapse function to see a bit better
    """Returns a random card"""
    return cards_list[random.randint(0, 8)]  # could have used random.choice(list)


def first_deal():
    """Deals out the first 2 cards but only shows 1 of the dealers"""
    player.extend([chose_card(), chose_card()])
    dealer.extend([chose_card(), chose_card()])
    print(f'Your cards are {player}')
    print(f"The dealer has a ['{dealer[0]}']")


def further_deal_player():
    """Appends a further card to player if he wishes"""
    player.append(chose_card())
    print(f'Your cards are {player}')


def further_deal_dealer():
    """Appends a further card of the dealer"""
    dealer.append(chose_card())


def cards_to_value(player_list, dealer_list):
    """Calculates the calue of the 2 decks"""
    player_score = 0
    dealer_score = 0
    for cards in player:
        player_score += cards_dictionary[
            cards]  # Could have used sum function!!: sum(list) sums up values and returns int.
    for cards in dealer:
        dealer_score += cards_dictionary[cards]
    if player_score > 21 and "Ace" in player:  # could also have used list.remove("Ace") followed by list.append ("1") to remove Ace if it is >21 and place a 1 instead
        player_score -= 10

    return player_score, dealer_score


def compare(player_score, dealer_score):
    """Compares values"""
    if player_score > dealer_score:
        print("You win! :)")
        print(f'Your score is {player_score}')
        print(f'The dealers cards are {dealer} and his score is {dealer_score}')

    elif player_score == dealer_score:
        print("Draw :|")
        print(f'Your score is {player_score}')
        print(f'The dealers cards are {dealer} and his score is {dealer_score}')

    elif player_score < dealer_score:
        print("You lose! :(")
        print(f'Your score is {player_score}')
        print(f'The dealers cards are {dealer} and his score is {dealer_score}')


def overshoot(player_score):
    """If player overshoots"""
    print("You lose, you overshot! :(")
    print(f'Your score is {player_score}')


def take_card():
    """Requests input if another card should be drawn"""
    take_card_output = input("Hit or Stand?\n")
    return take_card_output


def play_blackjack():
    """Initializes the game"""
    if take_card() == "Stand":

        player_score, dealer_score = cards_to_value(player, dealer)
        compare(player_score, dealer_score)

    else:
        further_deal_player()
        player_score, dealer_score = cards_to_value(player, dealer)
        if player_score > 21:
            overshoot(player_score)

        else:
            play_blackjack()

#--------Game-----#
print(logo)
first_deal()
play_blackjack()