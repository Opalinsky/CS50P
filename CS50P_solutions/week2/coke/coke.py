amount_due = 50
while amount_due > 0:
    print("Amount Due:", amount_due)
    insert_coin = int(input("Insert Coin: "))
    while amount_due > insert_coin:
        if insert_coin == 5 or insert_coin == 10 or insert_coin == 25:
            amount_due -= insert_coin
            break
        else:
            break
    else:
        change_owed = insert_coin-amount_due
        print("Change Owed:",change_owed)
        break


