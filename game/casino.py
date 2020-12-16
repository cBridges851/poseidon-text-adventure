import random
import time

class Casino:
    def print_cards(self, cards):
        '''
        Prints the cards of the given list.
        Args:
            cards: list, containing card values.
        '''
        for i in range(len(cards)):
            if i == len(cards) - 1:
                print(str(cards[i]), end=" ")
            else:
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
                value += i
            elif i == "A":
                value += 11
            else:
                value += 10
        return value
    
    def play_blackjack(self):
        '''
        Driver function for the game.
        Returns:
            W/L/D: string, the one returned depends on the result of the game.
        '''
        cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K","A","A","A","A"]
        dealer_cards = []
        player_cards = []
        card_index = random.randint(0,51)
        player_cards.append(cards.pop(card_index))
        card_index = random.randint(0,50)
        dealer_cards.append(cards.pop(card_index))
        card_index = random.randint(0, 49)
        player_cards.append(cards.pop(card_index))
        is_player_bust = False
        value = 0

        amount_of_cards = len(cards) - 1
        player_selection = ""
        print("------------------------------------------------------------------------------")
        while player_selection.upper() != "S":
            print("Dealer's cards: ")
            Casino().print_cards(dealer_cards)
            print("\nYour cards:")
            Casino().print_cards(player_cards)
            value = Casino().calc_card_value(player_cards)
            if value == 21:
                print("\nBlackJack!")
                return "W"
            player_selection = input("\nWould you like to hit(H) or stand(S): ").upper()
            print("------------------------------------------------------------------------------")
            if player_selection == "H":
                player_cards.append(cards.pop(random.randint(0, amount_of_cards)))
                amount_of_cards -= 1

                value = Casino().calc_card_value(player_cards)
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
                elif value == 21:
                    print("Your cards:")
                    Casino().print_cards(player_cards)
                    print("\nBlackJack!")
                    return "W"

        if is_player_bust == True:
            return "L"      
        else:
            while True:
                print("Dealer's cards: ")
                Casino().print_cards(dealer_cards)
                print("")
                dealer_val = Casino().calc_card_value(dealer_cards)
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
                if dealer_val > 16:
                    print("------------------------------------------------------------------------------")
                    print("Dealer stands")
                    if dealer_val > value:
                        print("Dealer wins")
                        return "L"
                    elif dealer_val < value:
                        print("You win!")
                        return "W"
                    else:
                        print("Draw!")
                        return "D"
                else:
                    dealer_cards.append(cards.pop(random.randint(0, amount_of_cards)))
                    amount_of_cards -= 1
                    time.sleep(1)
