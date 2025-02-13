import random

print("Welcome to Blackjack!!!")
card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = True
while play:
    blackjack = input("Enter 'yes' to play or 'no' to quit: ").lower()
    if blackjack == 'no':
        play = False
        break  # Exit the loop

    # Reset hands at the start of each round
    users_cards = []
    compute_cards = []

    # Draw initial cards
    users_cards.append(random.choice(card_deck))
    users_cards.append(random.choice(card_deck))

    compute_cards.append(random.choice(card_deck))  # Dealer shows one card
    compute_cards.append(random.choice(card_deck))  # Dealer's hidden card

    print(f"Your cards: {users_cards}, Sum: {sum(users_cards)}")
    print(f"Computer's first card: {compute_cards[0]}")

    # User's turn
    while sum(users_cards) < 21:
        draw_again = input("Do you want to draw another card? Type 'draw' or 'no': ").lower()
        if draw_again == 'draw':
            users_cards.append(random.choice(card_deck))
            # Adjust for Ace (11 -> 1 if over 21)
            if sum(users_cards) > 21 and 11 in users_cards:
                users_cards[users_cards.index(11)] = 1
            print(f"Your cards: {users_cards}, Sum: {sum(users_cards)}")
        else:
            break

    # Player bust check
    user_sum = sum(users_cards)
    if user_sum > 21:
        print("You bust! You lose. 😢")
    else:
        # Computer's turn: must draw if sum < 17
        while sum(compute_cards) < 17:
            compute_cards.append(random.choice(card_deck))
            if sum(compute_cards) > 21 and 11 in compute_cards:
                compute_cards[compute_cards.index(11)] = 1

        comp_sum = sum(compute_cards)
        print(f"Computer's cards: {compute_cards}, Sum: {comp_sum}")

        # Determine the winner
        if comp_sum > 21:
            print("Computer busts! You win! 🎉")
        elif user_sum > comp_sum:
            print("You win! 😃")
        elif user_sum < comp_sum:
            print("You lose. 😞")
        else:
            print("It's a draw! 🤝")

    # Ask to play again
    ch = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if ch == 'no':
        play = False






