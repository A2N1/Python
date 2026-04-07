import random

cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)

    if 11 in hand and score > 21:
        hand[hand.index(11)] = 1

    return sum(hand)

def show_hand(player, dealer, reveal_dealer=False):
    print("\nYour cards:", player, "Score:", calculate_score(player))
    
    if reveal_dealer:
        print("Dealer cards:", dealer, "Score:", calculate_score(dealer))
    else:
        print("Dealer first card:", dealer[0])

player_hand = [deal_card(), deal_card()]
dealer_hand = [deal_card(), deal_card()]

game_over = False

while not game_over:
    show_hand(player_hand, dealer_hand)

    if calculate_score(player_hand) > 21:
        print("💥 You went over 21! You lose.")
        break

    choice = input("Hit or Stand? (h/s): ").lower()

    if choice == "h":
        player_hand.append(deal_card())
    else:
        game_over = True

while calculate_score(dealer_hand) < 17:
    dealer_hand.append(deal_card())

show_hand(player_hand, dealer_hand, True)

player_score = calculate_score(player_hand)
dealer_score = calculate_score(dealer_hand)

if dealer_score > 21 or player_score > dealer_score:
    print("🎉 You win!")
elif player_score < dealer_score:
    print("😢 Dealer wins.")
else:
    print("🤝 Draw.")