import random

from prettytable import PrettyTable

count = 0

row_1 = [" ", "| |", " "]
row_2 = [" ", "| |", " "]
row_3 = [" ", "| |", " "]

it_is_draw = False
random_play = False

# ------------------------Conditions------------------------------------->


def conditions(item, player):
    if row_1[0] == item and row_1[1] == f"|{item}|" and row_1[2] == item:
        print(f"{player} won!!")
        return game()
    elif row_2[0] == item and row_2[1] == f"|{item}|" and row_2[2] == item:
        print(f"{player} won!!")
        return game()
    elif row_3[0] == item and row_3[1] == f"|{item}|" and row_3[2] == item:
        print(f"{player} won!!")
        return game()
    elif row_1[0] == item and row_2[0] == item and row_3[0] == item:
        print(f"{player} won!!")
        return game()
    elif row_1[1] == f"|{item}|" and row_2[1] == f"|{item}|" and row_3[1] == f"|{item}|":
        print(f"{player} won!!")
        return game()
    elif row_1[2] == item and row_2[2] == item and row_3[2] == item:
        print(f"{player} won!!")
        return game()
    elif row_1[0] == item and row_2[1] == f"|{item}|" and row_3[2] == item:
        print(f"{player} won!!")
        return game()
    elif row_1[2] == item and row_2[1] == f"|{item}|" and row_3[0] == item:
        print(f"{player} won!!")
        return game()
    elif count == 9:
        print("It's a Draw!!!!\n\n")
        play_again = input("\nWould you like to play again?\n\n").lower()
        if play_again == 'no':
            exit()
        elif not play_again == 'yes':
            print("Please enter a correct entry")
        else:
            global it_is_draw
            it_is_draw = True
            game()


def third_party(item):
    global count
    row = random.randint(1, 3)

    pos = random.randint(1, 3)-1

    if (row == 1 and row_1[pos] == "X"
            or row == 1 and row_1[pos] == "O"
            or row == 1 and row_1[pos] == "|X|"
            or row == 1 and row_1[pos] == "|O|"):
        return third_party(item)

    elif row == 1:
        if pos == 1:
            row_1[pos] = f"|{item}|"
            count += 1
        else:
            row_1[pos] = item
            count += 1

    if (row == 2 and row_2[pos] == "X"
            or row == 2 and row_2[pos] == "O"
            or row == 2 and row_2[pos] == "|X|"
            or row == 2 and row_2[pos] == "|O|"):
        return third_party(item)
    elif row == 2:
        if pos == 1:
            row_2[pos] = f"|{item}|"
            count += 1
        else:
            row_2[pos] = item
            count += 1

    if (row == 3 and row_3[pos] == "X"
            or row == 3 and row_3[pos] == "O"
            or row == 3 and row_3[pos] == "|X|"
            or row == 3 and row_3[pos] == "|O|"):
        return third_party(item)
    elif row == 3:
        if pos == 1:
            row_3[pos] = f"|{item}|"
            count += 1
        else:
            row_3[pos] = item
            count += 1
    print(
        f"\n\n{"  ".join(row_1)}\n<--------->\n"
        f"{"  ".join(row_2)}\n<--------->\n"
        f"{"  ".join(row_3)}"
    )


def player(item):
    global count
    try:
        row = int(input("Row(1 ,2 ,3): "))
        pos = int(input("\nPosition(1 ,2 ,3): ")) - 1

    except ValueError:
        player(item)
    else:
        if row > 3 or pos > 3:
            print("\nRow and position entry should be among 3.\n\n")
            player(item)
        elif (row == 1 and row_1[pos] == "X"
                or row == 1 and row_1[pos] == "O"
                or row == 1 and row_1[pos] == "|X|"
                or row == 1 and row_1[pos] == "|O|"):
            print("\nOps it has been already selected try again!!!\n\n")
            print(row_1)
            return player(item)

        elif row == 1:
            if pos == 1:
                row_1[pos] = f"|{item}|"
                count += 1
            else:
                row_1[pos] = item
                count += 1

        if (row == 2 and row_2[pos] == "X"
                or row == 2 and row_2[pos] == "O"
                or row == 2 and row_2[pos] == "|X|"
                or row == 2 and row_2[pos] == "|O|"):
            print("\nOps it has been already selected try again!!!\n\n")
            print(row_2)
            return player(item)
        elif row == 2:
            if pos == 1:
                row_2[pos] = f"|{item}|"
                count += 1
            else:
                row_2[pos] = item
                count += 1

        if (row == 3 and row_3[pos] == "X"
                or row == 3 and row_3[pos] == "O"
                or row == 3 and row_3[pos] == "|X|"
                or row == 3 and row_3[pos] == "|O|"):
            print("\nOps it has been already selected try again!!!\n\n")
            print(row_3)
            return player(item)
        elif row == 3:
            if pos == 1:
                row_3[pos] = f"|{item}|"
                count += 1
            else:
                row_3[pos] = item
                count += 1
        print(
            f"\n\n{"  ".join(row_1)}\n<--------->\n"
            f"{"  ".join(row_2)}\n<--------->\n"
            f"{"  ".join(row_3)}"
        )


def game():
    print("""
    ████████╗██╗ ██████╗    ████████╗ █████╗ ██╗  ██╗    ████████╗ ██████╗ ███████╗
    ╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██║ ██╔╝    ╚══██╔══╝██╔═══██╗██╔════╝
       ██║   ██║██║            ██║   ███████║█████╔╝        ██║   ██║   ██║█████╗  
       ██║   ██║██║            ██║   ██╔══██║██╔═██╗        ██║   ██║   ██║██╔══╝  
       ██║   ██║╚██████╗       ██║   ██║  ██║██║  ██╗       ██║   ╚██████╔╝███████╗
       ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝       ╚═╝    ╚═════╝ ╚══════╝

    """)
    global row_1, row_2, row_3, count, it_is_draw, random_play
    end = False

    count = 0
    row_1 = [" ", "| |", " "]
    row_2 = [" ", "| |", " "]
    row_3 = [" ", "| |", " "]
    if not it_is_draw:

        question = input("would you like to play? YES/NO: ").lower()
        if question == "no":
            exit()
        elif not question == 'yes':
            print("Please enter a correct entry")
            return game()
        third_party_player = input("would you like to play with a third_party? YES/NO: ").lower()
        if third_party_player == 'yes':
            random_play = True
        elif not third_party_player == 'no':
            print("Please enter a correct entry")
            return game()

    while not end:
        print("\nPlayer 1")
        player("X")
        conditions("X", "player 1")
        print("\nPlayer 2")
        if random_play:
            third_party("O")
            conditions("O", "Computer")
        else:
            player("O")
            conditions("O", "player 2")


game()

