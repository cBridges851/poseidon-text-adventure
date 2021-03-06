import random
import time
from components.file_logic import FileLogic
from components.text_delay import text_delay

PLAYER_FILENAME = "./player.json"

class Casino:
    def print_cards(self, cards):
        '''
            Prints the cards of the given list.  
            Args:
                cards: list, containing card values.
        '''
        for i in range(len(cards)):
            if i == len(cards) - 1:
                # Prints the card with a space after it if it is the last one
                print(str(cards[i]), end=" ")
            else:
                # Prints the card with a comma after it
                print(str(cards[i]), end=", ")
    
    def calc_card_value(self, cards):
        '''
            Calculates the value of the player's hand.  
            Args:
                cards: list, cards in the player's hand.
            Returns:
                value: int, value of the list.
        '''
        value = 0

        for i in cards:
            if isinstance(i, int):
                # If the card is an integer, the value is incremented by this number
                value += i
            elif i == "A":
                # Value is incremented by 11 if it is an ace
                value += 11
            else:
                # Value incremented by 10 otherwise
                value += 10

        return value
    
    def play_blackjack(self):
        '''
            Driver function for the game.  
            Returns:
                W/L/D: string, the one returned depends on the result of the game.
        '''
        # List of all cards
        cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K","A","A","A","A"]
        dealer_cards = []
        player_cards = []
        # Randomise the first set of cards given out.
        card_index = random.randint(0, 51)
        player_cards.append(cards.pop(card_index))
        card_index = random.randint(0, 50)
        dealer_cards.append(cards.pop(card_index))
        card_index = random.randint(0, 49)
        player_cards.append(cards.pop(card_index))
        is_player_bust = False
        value = 0

        amount_of_cards = len(cards) - 1
        player_selection = ""
        print("------------------------------------------------------------------------------")

        # Loops until the player chooses to stand
        while player_selection.upper() != "S":
            # Print the first set of cards.
            print("Dealer's cards: ")
            Casino().print_cards(dealer_cards)
            print("\nYour cards:")
            Casino().print_cards(player_cards)
            value = Casino().calc_card_value(player_cards)

            if value == 21:
                print("\nBlackJack!")
                return "W"

            # Decide the players action.
            player_selection = input("\nWould you like to hit(H) or stand(S): ").upper()
            print("------------------------------------------------------------------------------")

            if player_selection == "H":
                player_cards.append(cards.pop(random.randint(0, amount_of_cards)))
                amount_of_cards -= 1
                value = Casino().calc_card_value(player_cards)

                # Player goes bust if the value is above 21
                if value > 21:
                    if "A" in player_cards:
                        value -= 10
                        if value > 21:
                            print("Your cards:")
                            Casino().print_cards(player_cards)
                            print("\nBust, you lose")
                            is_player_bust = True
                            break
                    else:
                        print("Your cards:")
                        Casino().print_cards(player_cards)
                        print("\nBust, you lose")
                        is_player_bust = True
                        break
                # Player wins if the value is exactly 21
                elif value == 21:
                    print("Your cards:")
                    Casino().print_cards(player_cards)
                    print("\nBlackJack!")
                    return "W"

        # Returns that the player lost if they went bust
        if is_player_bust:
            return "L"

        else:
            while True:
                # If the player stands load the dealer logic.
                print("Dealer's cards: ")
                Casino().print_cards(dealer_cards)
                print("")
                dealer_val = Casino().calc_card_value(dealer_cards)

                # If the dealers card values are above 21 the player wins.
                if dealer_val > 21:
                    print("------------------------------------------------------------------------------")

                    if "A" in dealer_cards:
                        dealer_val -= 10
                        if dealer_val > 21:
                            print("Dealer busts, you win!")
                            return "W"
                    else:
                        print("Dealer busts, you win!")
                        return "W"
                
                # If the dealers card value is above 16 from the first round, stand.
                if dealer_val > 16:
                    print("------------------------------------------------------------------------------")
                    print("Dealer stands")
                    # Check who wins.
                    if dealer_val > value:
                        print("Dealer wins")
                        return "L"
                    elif dealer_val < value:
                        # Returns that the player has won
                        print("You win!")
                        return "W"
                    else:
                        # Returns that the game resolved to a draw
                        print("Draw!")
                        return "D"
                else:
                    # Get a new card for the dealer.
                    dealer_cards.append(cards.pop(random.randint(0, amount_of_cards)))
                    amount_of_cards -= 1
                    time.sleep(1)
    
    def better_and_runner(self, player):
        '''
            Introduces the player to the casino and gets the number of coins  
            they wish to bet.  
            Args: 
                player: obj, representing a player.
        '''
        text_delay("Welcome to the casino! Here, you can play blackjack: ")
        in_casino = True

        # Loops until the player leaves the casino
        while in_casino:
            user_input = ""

            # Decide whether the player wants to play.
            while user_input != "Y" and user_input != "N":
                user_input = input("Would you like to play?(Y/N): ").upper()

            if user_input == "Y":
                game_result = ""

                while True:
                    print("------------------------------------------------------------------------------")
                    bet = ""
                    
                    # Bet validation by checking if it is an integer
                    while not isinstance(bet, int):
                        try:
                            bet = int(input("How much do you want to bet? "))
                        except Exception:
                            print("Invalid bet!")

                    # For if the player does not have any coins
                    if player.coins <= 0:
                        text_delay("The casino manager yells at you saying you can't play without any coins. Beat it scum!")
                        break
                    # For if the player inputs more coins than they actually have
                    elif bet > player.coins:
                        text_delay("You don't have enough coins for this bet.")
                        break
                    # Allows the player to proceed with the game
                    else:
                        text_delay(f"Taken {bet} coins from your inventory.")
                        player.coins -= bet
                        FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
                        game_result = Casino().play_blackjack()
                        break

                # Update the players coins based off the game result.
                if game_result == "W":
                    # Player gets double their bet
                    player.coins += bet * 2
                    FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
                    text_delay("You doubled your bet. Added your earnings to your inventory.")
                elif game_result == "L":
                    text_delay("You lost your bet.")
                elif game_result == "D":
                    player.coins += bet
                    FileLogic().update_player_property(PLAYER_FILENAME, player, "Coins", player.coins)
                    text_delay("Bet returned to your inventory.")
                print("------------------------------------------------------------------------------")

            if user_input == "N":
                text_delay("Okay, thanks for coming!")
                in_casino = False
