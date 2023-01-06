import random
while True:

    def game(comp,you):
        if (comp == you):
            return None

        # first condition

        elif comp == "s":
            if you =="w":
                return False
            elif you == "g":
                return True

        # second condition

        elif comp == "w":
            if you == "g":
                return False
            elif you == "s":
                return True

        # thr`d condition

        elif comp == "g":
            if you == "s":
                return False
            elif you == "w":
                return True


    random_no = random.randint(1, 3)
    print("comp:turn snake(s),water(w)and gun(g)")
    if random_no == 1:
        comp = "s"
    elif random_no == 2:
        comp = "w"
    elif random_no == 3:
        comp = "g"

    you = input("your turn:snake(s),water(w)and gun(g)")

    a = game(comp, you)
    print(comp)
    print(you)

    if a == None:
        print("game is tie")
    elif a:
        print("you win")
    else:
        print("you lose")












