def diceroller():
    import random
    while True:
        input("Press Enter to roll the dice")
        print("you rolled a ", random.randint(1, 6))
        again = input("Roll again? (y/n):")
        if again.lower() != 'y':
            break

diceroller()