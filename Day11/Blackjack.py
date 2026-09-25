import random


CARDS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
CARD_VALUES = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}


def draw_card():
    return random.choice(CARDS)


def score_hand(hand):
    score = sum(CARD_VALUES[card] for card in hand)
    aces = hand.count("A")

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score


def is_blackjack(hand):
    return len(hand) == 2 and score_hand(hand) == 21


def can_split(hand):
    return len(hand) == 2 and CARD_VALUES[hand[0]] == CARD_VALUES[hand[1]]


def get_yes_or_no(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ["y", "n"]:
            return choice
        print("Please type 'y' or 'n'.")


def get_bet(money, prompt="Enter your bet amount: Rs."):
    while True:
        try:
            bet = int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if bet <= 0:
            print("Your bet must be more than Rs.0.")
        elif bet > money:
            print("You don't have enough money to place that bet.")
        else:
            return bet


def play_hand(hand, bet, money, hand_name="Your hand"):
    surrendered = False
    first_choice = True

    while score_hand(hand) < 21:
        actions = ["h", "s"]

        if first_choice and money >= bet:
            actions.append("d")

        if first_choice:
            actions.append("r")

        prompt = "Type 'h' to hit, 's' to stand"
        if "d" in actions:
            prompt += ", 'd' to double down"
        if "r" in actions:
            prompt += ", or 'r' to surrender"
        prompt += ": "

        choice = input(prompt).lower()

        if choice not in actions:
            print("That action is not available right now.")
            continue

        if choice == "h":
            hand.append(draw_card())
            print(f"{hand_name}: {hand}, score: {score_hand(hand)}")
        elif choice == "s":
            break
        elif choice == "d":
            money -= bet
            bet *= 2
            hand.append(draw_card())
            print(f"{hand_name}: {hand}, score: {score_hand(hand)}")
            break
        elif choice == "r":
            surrendered = True
            break

        first_choice = False

    return {
        "hand": hand,
        "bet": bet,
        "money": money,
        "surrendered": surrendered,
    }


def settle_hand(result, dealer_cards, money):
    hand = result["hand"]
    bet = result["bet"]
    player_score = score_hand(hand)
    dealer_score = score_hand(dealer_cards)

    print(f"Your final hand: {hand}, final score: {player_score}")

    if result["surrendered"]:
        refund = bet // 2
        print(f"You surrendered. Rs.{refund} is returned.")
        return money + refund

    if player_score > 21:
        print("You went over. You lose.")
    elif dealer_score > 21:
        print("Dealer went over. You win.")
        money += bet * 2
    elif player_score > dealer_score:
        print("You win.")
        money += bet * 2
    elif player_score < dealer_score:
        print("You lose.")
    else:
        print("Push. Your bet is returned.")
        money += bet

    return money


print("Welcome to the Blackjack game!")
print("+---------+")
print("| A       |")
print("|         |")
print("|    S    |")
print("|         |")
print("|       A |")
print("+---------+")

money = 1000

while money > 0:
    choice = get_yes_or_no("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if choice == "n":
        break

    print(f"You have Rs.{money} to play with.")
    bet = get_bet(money)
    money -= bet

    player_cards = [draw_card(), draw_card()]
    dealer_cards = [draw_card(), draw_card()]
    insurance_bet = 0

    print(f"Your cards: {player_cards}, current score: {score_hand(player_cards)}")
    print(f"Dealer's face-up card: {dealer_cards[0]}")
    print("Dealer's second card is face down.")

    if dealer_cards[0] == "A" and money > 0 and bet // 2 > 0:
        insurance_choice = get_yes_or_no("Dealer shows an Ace. Do you want insurance? Type 'y' or 'n': ")
        if insurance_choice == "y":
            max_insurance = min(bet // 2, money)
            insurance_bet = get_bet(max_insurance, f"Enter insurance bet up to Rs.{max_insurance}: ")
            money -= insurance_bet

    player_blackjack = is_blackjack(player_cards)
    dealer_blackjack = is_blackjack(dealer_cards)

    if dealer_blackjack:
        print(f"Dealer reveals: {dealer_cards}, score: {score_hand(dealer_cards)}")
        if insurance_bet > 0:
            print("Insurance wins and pays 2:1.")
            money += insurance_bet * 3
    elif insurance_bet > 0:
        print("Dealer does not have blackjack. Insurance bet is lost.")

    if player_blackjack or dealer_blackjack:
        if player_blackjack and dealer_blackjack:
            print("Both have blackjack. Push.")
            money += bet
        elif player_blackjack:
            payout = bet + int(bet * 1.5)
            print("Blackjack! It pays 3:2.")
            money += payout
        else:
            print("Dealer has blackjack. You lose.")

        print(f"You have Rs.{money} left.")
        continue

    player_results = []

    if can_split(player_cards) and money >= bet:
        split_choice = get_yes_or_no("You can split this pair. Type 'y' to split or 'n' to continue: ")
        if split_choice == "y":
            money -= bet
            hands = [[player_cards[0], draw_card()], [player_cards[1], draw_card()]]
            for hand_number, hand in enumerate(hands, start=1):
                print(f"Playing hand {hand_number}: {hand}, score: {score_hand(hand)}")
                result = play_hand(hand, bet, money, f"Hand {hand_number}")
                money = result["money"]
                player_results.append(result)
        else:
            result = play_hand(player_cards, bet, money)
            money = result["money"]
            player_results.append(result)
    else:
        result = play_hand(player_cards, bet, money)
        money = result["money"]
        player_results.append(result)

    active_hands = [
        result
        for result in player_results
        if not result["surrendered"] and score_hand(result["hand"]) <= 21
    ]

    if active_hands:
        print(f"Dealer reveals: {dealer_cards}, score: {score_hand(dealer_cards)}")
        while score_hand(dealer_cards) <= 16:
            dealer_cards.append(draw_card())
            print(f"Dealer draws: {dealer_cards}, score: {score_hand(dealer_cards)}")
    else:
        print(f"Dealer's hand: {dealer_cards}, score: {score_hand(dealer_cards)}")

    print(f"Dealer's final hand: {dealer_cards}, final score: {score_hand(dealer_cards)}")

    for result in player_results:
        money = settle_hand(result, dealer_cards, money)

    print(f"You have Rs.{money} left.")

print(f"Thanks for playing. You leave with Rs.{money}.")
