def Game(n):
    import random
    list = ['r','p','s']
    chances = 10
    Computer = 0
    You = 0
    Tied = 0
    while chances > 0:
        u = input("Enter r for Rock and p for Paper and s for Scissor : ")
        c = random.choice(list)

        if u == c:
            Tied = Tied + 1
            print("Game Tied 0 points to both")
            print(f"Your Guess is {u} and Computer Guess is {c}")
            print(f"Computer points : {Computer}")
            print(f"Your Points : {You}")
            print(f"Tied Game : {Tied}")

        # if you choose rock
        elif u =='r' and c =='p':
            Computer = Computer + 1
            print("Computer Wins 1 points")
            print(f"Your Guess is {u} and Computer Guess is {c}")
            print(f"Computer points : {Computer}")
            print(f"Your Points : {You}")
            print(f"Tied Game : {Tied}")

        elif u == 'r' and c == 's':
            You = You + 1
            print("You Wins 1 points")
            print(f"Your Guess is {u} and Computer Guess is {c}")
            print(f"Computer points : {Computer}")
            print(f"Your Points : {You}")
            print(f"Tied Game : {Tied}")

        # if you choose scissor
        elif u == 's' and c == 'p':
            You = You + 1
            print("You Wins 1 points")
            print(f"Your Guess is {u} and Computer Guess is {c}")
            print(f"Computer points : {Computer}")
            print(f"Your Points : {You}")
            print(f"Tied Game : {Tied}")

        elif u == 's' and c == 'r':
            Computer = Computer + 1
            print("Computer Wins 1 points")
            print(f"Your Guess is {u} and Computer Guess is {c}")
            print(f"Computer points : {Computer}")
            print(f"Your Points : {You}")
            print(f"Tied Game : {Tied}")

        #if you chose paper
        elif u == 'p' and c == 's':
            Computer = Computer + 1
            print("Computer Wins 1 points")
            print(f"Your Guess is {u} and Computer Guess is {c}")
            print(f"Computer points : {Computer}")
            print(f"Your Points : {You}")
            print(f"Tied Game : {Tied}")

        elif u == 'p' and c == 'r':
            You = You + 1
            print("You Wins 1 points")
            print(f"Your Guess is {u} and Computer Guess is {c}")
            print(f"Computer points : {Computer}")
            print(f"Your Points : {You}")
            print(f"Tied Game : {Tied}")

        else:
            print("Invalid Option")
        chances = chances - 1
        print(f"chances left : {chances}""\n")

    print("Game Over")
    if Computer > You:
        print("You Lose")
    elif You > Computer:
        print("You Win")
    else:
        print("Game Tied")
    print(f"Computer Score : {Computer} and Your Score : {You} and Tied Score : {Tied} ")


if __name__ == '__main__':
    restart = ('Y')
    while restart != ['n', 'N', 'no', 'NO']:
        a = input("Press Enter To Play")
        m = Game(a)
        restart = input("Press Y to Play Again : ")
        if restart in ['n', 'N', 'no', 'NO']:
            print("Thank You for Playing")
            break


