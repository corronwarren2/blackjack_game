#Python Blackjack
#For this project you will make a Blackjack game using Python. Click here to
#familiarize yourself with the the rules of the game. You won't be implementing' \
#' every rule "down to the letter" with the game, but we will doing a ' \
#'simpler version of the game. This assignment will be given to further test' \
# your knowledge on object-oriented programming concepts.

#Rules:
#1. The game will have two players: the Dealer and the Player.
# The game will start off with a deck of 52 cards.
# The 52 cards will consist of 4 different suits: Clubs, Diamonds,
# Hearts and Spades. For each suit, there will be cards numbered 1 through 13.
#Note: No wildcards will be used in the program

#2. When the game begins, the dealer will shuffle the deck of cards,
# making them randomized. After the dealer shuffles, it will deal the player 2
# cards and will deal itself 2 cards from. The Player should be able to see
# both of their own cards, but should only be able to see one of the
# Dealer's cards.

#3. The objective of the game is for the Player to count their cards after
# they're dealt. If they're not satisfied with the number, they have the
# ability to 'Hit'. A hit allows the dealer to deal the Player one
# additional card. The Player can hit as many times as they'd like as
# long as they don't 'Bust'. A bust is when the Player is dealt cards
# that total more than 21.

#4. If the dealer deals the Player cards equal to 21 on the first deal,
# the Player wins. This is referred to as Blackjack. Blackjack is NOT the
# same as getting cards that equal up to 21 after the first deal. Blackjack
# can only be attained on the first deal.

#5. The Player will never see the Dealer's hand until the Player chooses to
# 'stand'. A Stand is when the player tells the dealer to not deal it anymore
# cards. Once the player chooses to Stand, the Player and the Dealer will
# compare their hands. Whoever has the higher number wins. Keep in mind that
# the Dealer can also bust.

#import random
#suits = ['hearts', 'spades', 'clubs', 'diamonds']
#values = [1, 2, 3, 4]
#cards = [(suit, value) for suit in suits for value in values]
#print('Before shuffle')
#print(cards)
#random.shuffle(cards)
#print('After Shuffle')
#print(cards)





import random


# Blackjack or 21 game


dealers_cards = []

players_cards =[]

# Dealers Cards
while len(dealers_cards) != 2:
    dealers_cards.append(random.randint(1,11))
    if len(dealers_cards) == 2:
        print("Dealer has: X ,", dealers_cards[1])
# Players cards
while len(players_cards) != 2:
    players_cards.append(random.randint(1,11))
    if len(players_cards) == 2:
        print("You have: ", players_cards)



#Sum of Dealers Cards
if sum(dealers_cards) == 21:
    print("Dealer has 21 and wins!")
elif sum(dealers_cards) > 21:
    print("Dealer has busted!")

#Sum of Players Cards
while sum(players_cards) == 21:
    print("BLACKJACK! YOU WIN!!! 21!")


while sum(players_cards) < 21:
    action_taken = str(input("Do you want to stay or hit?  "))
    if action_taken == "hit":
        players_cards.append(random.randint(1,11))
        print("You now have a total of " + str(sum(players_cards)) + " from these cards", players_cards)
    else:
        print("The dealer has a total of " + str(sum(dealers_cards)) + "with ", dealers_cards)
        print("You have a total of " + str(sum(players_cards)) + "with", players_cards)
        if sum(dealers_cards) > sum(players_cards):
            print("Dealer Wins! Better luck next time!")
            break
    while action_taken == "stay":
        if sum(players_cards) > 21:
            print("You BUSTED. Better luck next time!")

        if sum(dealers_cards) == sum(players_cards):
            print(" Push!")

        elif sum(players_cards) == 21:
            print("BLACKJACK! YOU WIN!!! 21!")
            break
# compare the sum of the cards D V P

# if P card sum is greater than 21 = bust

# if P card sum is less than 21 = Option Hit or Stay

# if P option Stay compare sum of D V P

# If P sum < 21 && > D sum then P wins

# If P sum < D sum then P loses


