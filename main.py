import numpy as np
from time import sleep
class Chip:
    def __init__(self, total=100):
        self.total = total  
    def win(self, bet):
        self.total += bet
    def lose(self, bet):
        self.total -= bet
def draw_card(cards,qty,a):
    i = 0
    for x in cards.copy():
        a = np.append(a,x)
        cards.remove(x)
        if i >= qty - 1:
            break
        i += 1
    return a
def total_cards(cards):
    x = ''
    y = ''
    for i in range(len(cards)):
        for j in range(len(cards[i])):
            if cards[i][j] == "♥" or cards[i][j] == "♠" or cards[i][j] == "♣" or cards[i][j] == "♦":
                break
            else:
                y += cards[i][j]
    x += y
    z = 0
    temp = ''
    for i in range(len(x)):
        if x[i] == "K" or x[i] == "Q" or x[i] == "J":
            z += 10
        elif x[i] == "A":
            if z < 11:
                z += 11
            else:
                z +=  1
        else:
            if x[i] == "1":
                z += 10
            else:
                z += int(x[i])
    return z
def reveal_cards(a,a_total,a_name,b,b_total,b_name):
    sleep(0.5)
    print("="*80)
    print("Revealing cards...")
    print("="*80)
    print()
    print(f"{a_name.capitalize()} = {a} \nTotal = {a_total}\n")
    print(f"{b_name.capitalize()} = {b} \nTotal = {b_total}")
def take_turns(a,a_total,a_name,opponent,opponent_total,opponent_name,cards,move,money,bet,total):
    status = ''
    print()
    sleep(2.5)
    if a_name == "player":
        if a_total == 21 and (move == 2 or move == 3) and a_total != opponent_total:
            reveal_cards(a,a_total,a_name,opponent,opponent_total,opponent_name)
            status = a_name.capitalize() + " BLACKJACK!"
            money.win(bet)
            return status
        elif a_total > 21:
            reveal_cards(a,a_total,a_name,opponent,opponent_total,opponent_name)
            status = a_name.capitalize() + " Busts, " + opponent_name.capitalize() + " Wins"
            money.lose(bet)
            return status
        elif opponent_total > 21:
            reveal_cards(a,a_total,a_name,opponent,opponent_total,opponent_name)
            status = opponent_name.capitalize() + " Busts, " + a_name.capitalize() + " Wins"
            money.win(bet)
            return status
        elif a_total > opponent_total and a_total < 21 and (move == 2 or move == 3) and opponent_total >= 17:
            reveal_cards(a,a_total,a_name,opponent,opponent_total,opponent_name)
            status = a_name.capitalize() + " Wins"
            money.win(bet)
            return status
        elif a_total == opponent_total and (move == 2 or move == 3):
            reveal_cards(a,a_total,a_name,opponent,opponent_total,opponent_name)
            status = "Push"
            return status
        elif a_total < opponent_total and opponent_total < 21 and (move == 2 or move == 3) and opponent_total >= 17:
            reveal_cards(a,a_total,a_name,opponent,opponent_total,opponent_name)
            status = opponent_name.capitalize() + " Wins"
            money.lose(bet)
            return status
        else:
            double = ''
            if move == 1:
                double = "-"
                move = 0
            while(move != 1 and move !=2 and move!=3 ):
                print("Player's Turn")
                print("*************\n")
                if (double == ''):
                    print("Do you want to hit, stand, or double?")
                    print("1. Hit")
                    print("2. Stand")
                    print("3. Double")
                else:
                    print("Do you want to hit or stand?")
                    print("1. Hit")
                    print("2. Stand")
                move = int(input("Pick one = "))
                if move == 1:
                    print("\nPlayer has decided to hit.\n")
                    a = draw_card(cards,1,a)
                    a_total = total_cards(a)
                    print("Player's cards =",a,"\nTotal =",a_total)
                    print(f"Dealer's cards = [{opponent[0]}" + ", ?" * (len(opponent)-1) + "]\nTotal = unknown")
                    temp = a
                    a = opponent
                    opponent = temp
                    temp = a_total
                    a_total = opponent_total
                    opponent_total = temp
                    temp = a_name
                    a_name = opponent_name
                    opponent_name = temp
                    return take_turns(a,a_total,a_name,opponent,opponent_total,opponent_name,cards,move,money,bet,total)
                elif move == 2:
                    print("\nPlayer has decided to stand.")
                    temp = a
                    a = opponent
                    opponent = temp
                    temp = a_total
                    a_total = opponent_total
                    opponent_total = temp
                    temp = a_name
                    a_name = opponent_name
                    opponent_name = temp
                    return take_turns(a,a_total,a_name,opponent,opponent_total,opponent_name,cards,move,money,bet,total)
                elif (move == 3) and (double == ''):
                    if ((bet*2) > total):
                        print("The amount of chips you own is not enough to double your bet. Try again")
                        move = 0
                        return take_turns(a,a_total,a_name,opponent,opponent_total,opponent_name,cards,move,money,bet,total)
                    else:
                        bet*=2
                        double = "-"
                        a = draw_card(cards,1,a)
                        a_total = total_cards(a)
                        print("\nPlayer has decided to double. The player cannot take anymore cards.\n")
                        print("Player's cards =",a,"\nTotal =",a_total)
                        print(f"Dealer's cards = [{opponent[0]}" + ", ?" * (len(opponent)-1) + "]\nTotal = unknown")
                        temp = a
                        a = opponent
                        opponent = temp
                        temp = a_total
                        a_total = opponent_total
                        opponent_total = temp
                        temp = a_name
                        a_name = opponent_name
                        opponent_name = temp
                        return take_turns(a,a_total,a_name,opponent,opponent_total,opponent_name,cards,move,money,bet,total)
                else:
                    print("\nAnswer isn't valid. Reenter answer.\n")
                    move = 0
    elif a_name == "dealer":
        if opponent_total == 21 and (move == 2 or move == 3) and a_total != opponent_total:
            reveal_cards(opponent,opponent_total,opponent_name,a,a_total,a_name)
            status = opponent_name.capitalize() + " BLACKJACK!"
            money.win(bet)
            return status
        if a_total == 21 and (move == 2 or move == 3) and a_total != opponent_total:
            reveal_cards(opponent,opponent_total,opponent_name,a,a_total,a_name)
            status = a_name.capitalize() + " BLACKJACK!"
            money.lose(bet)
            return status
        elif a_total > 21:
            reveal_cards(opponent,opponent_total,opponent_name,a,a_total,a_name)
            status = a_name.capitalize() + " Busts, " + opponent_name.capitalize() + " Wins"
            money.win(bet)
            return status
        elif opponent_total > 21:
            reveal_cards(opponent,opponent_total,opponent_name,a,a_total,a_name)
            status = opponent_name.capitalize() + " Busts, " + a_name.capitalize() + " Wins"
            money.lose(bet)
            return status
        elif a_total < opponent_total and opponent_total < 21 and (move == 2 or move == 3) and a_total >= 17:
            reveal_cards(opponent,opponent_total,opponent_name,a,a_total,a_name)
            status = opponent_name.capitalize() + " Wins"
            money.win(bet)
            return status
        elif a_total > opponent_total and (move == 2 or move == 3) and a_total < 21 and a_total >= 17:
            reveal_cards(opponent,opponent_total,opponent_name,a,a_total,a_name)
            status = a_name.capitalize() + " Wins"
            money.lose(bet)
            return status
        elif a_total == opponent_total and (move == 2 or move == 3):
            reveal_cards(a,a_total,a_name,opponent,opponent_total,opponent_name)
            status = "Push"
            return status
        else:
            print("Dealer's Turn")
            print("*************\n")
            if a_total < 17:
                print("Dealer has drawn a card from the deck.\n")
                a = draw_card(cards,1,a)
                a_total = total_cards(a)
                print("Player's cards =",opponent,"\nTotal =",opponent_total)
                print(f"Dealer's cards = [{a[0]}" + ", ?" * (len(a)-1) + "]\nTotal = unknown")
                if move == 2 or move == 3:
                    return take_turns(a,a_total,a_name,opponent,opponent_total,opponent_name,cards,move,money,bet,total)
                else:
                    temp = a
                    a = opponent
                    opponent = temp
                    temp = a_total
                    a_total = opponent_total
                    opponent_total = temp
                    temp = a_name
                    a_name = opponent_name
                    opponent_name = temp
                    return take_turns(a,a_total,a_name,opponent,opponent_total,opponent_name,cards,move,money,bet,total)
            else:
                print("Dealer has decided to stand.\n")
                print("Player's cards =",opponent,"\nTotal =",opponent_total)
                print(f"Dealer's cards = [{a[0]}" + ", ?" * (len(a)-1) + "]\nTotal = unknown")
            if move != 2 or move != 3:
                temp = a
                a = opponent
                opponent = temp
                temp = a_total
                a_total = opponent_total
                opponent_total = temp
                temp = a_name
                a_name = opponent_name
                opponent_name = temp
                return take_turns(a,a_total,a_name,opponent,opponent_total,opponent_name,cards,move,money,bet,total)
            elif a_total == 21 and a_total != opponent_total:
                reveal_cards(opponent,opponent_total,opponent_name,a,a_total,a_name)
                status = a_name.capitalize() + " BLACKJACK!"
                money.lose(bet)
                return status
            elif a_total > 21:
                reveal_cards(opponent,opponent_total,opponent_name,a,a_total,a_name)
                status = a_name.capitalize() + " Busts, " + opponent_name.capitalize() + " Wins"
                money.win(bet)
                return status
            elif opponent_total > 21:
                reveal_cards(opponent,opponent_total,opponent_name,a,a_total,a_name)
                status = opponent_name.capitalize() + " Busts, " + a_name.capitalize() + " Wins"
                money.lose(bet)
                return status
            elif a_total > opponent_total and a_total < 21 and (move == 2 or move == 3):
                reveal_cards(opponent,opponent_total,opponent_name,a,a_total,a_name)
                status = a_name.capitalize() + " Wins"
                money.lose(bet)
                return status
            elif a_total < opponent_total and opponent_total < 21 and (move == 2 or move == 3):
                reveal_cards(opponent,opponent_total,opponent_name,a,a_total,a_name)
                status = opponent_name.capitalize() + " Wins"
                money.win(bet)
                return status
            elif a_total == opponent_total and (move == 2 or move == 3) and a_total >= 17:
                reveal_cards(opponent,opponent_total,opponent_name,a,a_total,a_name)
                status = "Push"
                return status
    if a_total == opponent_total:
        reveal_cards(a,a_total,a_name,opponent,opponent_total,opponent_name)
        status = "Push"
    return status
card_num = np.array(["2","3","4","5","6","7","8","9","10","A","K","Q","J"])
card_shape = np.array(["♥","♠","♣","♦"])
deck = set()
def start(deck):
    chips=Chip()
    print('='*80)
    print("♥ ♦ THE GAME BEGINS ♠ ♣")
    print("Your Starter Chips = ",chips.total)
    print('='*80)
    while True:
        if len(deck) <= 6:
            for i in range(len(card_num)):
                for j in range(len(card_shape)):
                    temp = card_num[i] + card_shape[j]
                    deck.add(temp)
        player = np.array([])
        dealer = np.array([])
        player = draw_card(deck,2,player)
        player_total = total_cards(player)
        dealer = draw_card(deck,2,dealer)
        dealer_total = total_cards(dealer)
        move = 0
        print('\nYour goal is to collect 500 chips to win this game.')
        bid=int(input("Bid = "))
        if bid > chips.total:
            print("You are not allowed to bid more than the amount of chips you own. Try again.")
            print('='*80)
            print()
        elif bid < 20:
            print()
            print("The minimum amount to bid is 20 chips.")
            print("="*80)
        else:
            print("\nYou have been given 2 cards.\n")
            print("Player's cards =",player,"\nTotal =",player_total)
            print(f"Dealer's cards = ['{dealer[0]}', ?]\nTotal = unknown")
            winner = take_turns(player,player_total,"player",dealer,dealer_total,"dealer",deck,move,chips,bid,chips.total)
            print("\nStatus =",winner)
            print('='*80)
            print('Your Chips = ',chips.total)
            print('='*80)
            if chips.total >= 500:
                print('The dealer has lost all of his money, please come back later...')
                print()
                break
            elif chips.total < 20:
                print('You have run out of chips to bet. You are such a noob at BlackJack. Please Exit ')
                print()
                break
def tutor():
    print()
    print("♥ ♦ BLACKJACK TUTORIAL ♠ ♣")
    print("="*80)
    print("\nCard Values")
    print("***********")
    print("\nAce cards (A) can be counted as 1 or 11. \nThe value of the King (K), Queen (Q), and Jack (J) card is 10")
    print("2-10 cards match the number values printed on the cards.")
    print()
    print("How to play")
    print("***********")
    print()
    print("1. At the start of the game we receive 100 chips. Chip is a transaction system used in the game to determine how much you bet in one game")
    print()
    print("2. Your goal is to win the game by collecting at least 500 chips")
    print()
    print("3. The user will input the amount of chips to bet")
    print("--> The minimum amount of chips you can input is 20 \n--> Whereas the maximum chips you can input is the amount chips you currently have.")
    print()
    print("4. After that, the BlackJack match begins. In this match there will be two players competing, namely the Player and Dealer.")
    print("--> The player is you, the user, and the dealer is your opponent (the program)")
    print()
    print("5. The system will automatically give the player and the dealer 2 cards from the deck and you will be able to see what cards you have gotten and the total of the cards")
    print("--> However, the dealer's cards will also appear on screen, only displaying one of their cards while the rest are hidden.")
    print("--> The dealer's total cards will be labeled 'Unknown' until the game ends")
    print()
    print("6. Then the player will play first")
    print()
    print("7. PLayer get to choose whether they want to hit, stand, or double")
    print("--> Hit is when the player wants to add a new card to an existing deck until they decide to stand. \n--> Stand is when the player doesn't want to add cards and their turn will be over. \n--> Double is when the player can only add 1 card and doubling their bet, thus their turn is over.")
    print("--> The dealer can independently Hit or Stand")
    print()
    print("8. If the player hits and the total cards exceed 21 (BlackJack) then both the player and the dealer will reveal their cards")
    print("--> All of the dealer's cards will be visible, and with the total dealer will issue the appropriate result")
    print()
    print("9. Then a status will appear indicating who is the winner. (ex : Status = Player Busts, Dealer Wins)")
    print()
    print("--> Bust      = Cards exceeding 21 (Blackjack)")
    print("--> Blackjack = Total cards are exactly 21")
    print("--> Win       = Total cards are higher than the opponent but still under 21")
    print()
    print("10. After the winner in one match has been determined, the Player Chips will increase or decrease according to the bid/bet that was adjusted at the beginning of the game.")
    print("--> If, for example, the initial bid is 50, then whoever wins will receive 50 chips.")
    print()
    print("11. The system will return to the initial menu to show the remaining chips and determine the bid for the next match.")
    print()
    print("12. If the remaining chips reach 0 then the system will finish with the message that you are lost and weak in this game.")
    print()
    print("13. If the remaining chips reach or are more than 500, the system will be finished with a message that the dealer has run out of money and is asked to come back later.")
    print()
    r = 'y'
    while r == 'y':
        rr = input("Ready to play ? (y/n)").lower()
        if rr == 'y':
            start(deck)
            print()
            break
        elif rr == 'n':
            print()
            t = input("Do you want to see the tutorial again ? (y/n)").lower()
            if t == 'y':
                tutor()
                break
            elif t == 'n':
                print("We will play the game")
                print()
                start(deck)
                break
            else:
                print("Wrong code. You will return to main menu")
                print()
                break
            break
        else:
            print('Wrong code')
            print()
pil = 0
while pil != '3':
    print("♥ ♦ WELCOME TO BLACKJACK GAME ♠ ♣")
    print("="*80)
    print("1. Start the game")
    print("2. Tutorial")
    print("3. Exit the game")
    pil = input("Enter your choice (1-3) = ")
    print()
    if pil != 3:
        if pil == '1':
            tmbh = 'y'
            cnt = 3
            while tmbh == 'y':
                pil1 = input("Do you want to see the tutorial first (y/n) ? ").lower()
                if pil1 == 'y':
                    tutor()
                    break
                elif pil1 =='n':
                    print()
                    start(deck)
                    print()
                    break
                else:
                    if cnt > 1:
                        print("You entered the wrong code. You have two tries left.")
                        print()
                        cnt -= 1
                    elif cnt == 1:
                        print("You have entered the wrong code many times. You will return to the main menu")
                        print()
                        break
        elif pil == '2':
            tutor()
        elif pil != '3':
            print("You entered the wrong code\n")
print("Thank you for playing the game")
