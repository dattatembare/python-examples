def number_of_coins(centes_in, coins):
    coins_dict = {}
    for coin in coins:
        if coin <= centes_in:
            coins_dict[coin] = centes_in // coin
            centes_in = centes_in % coin
    return coins_dict


available_coins = [25, 10, 5, 1]
print(number_of_coins(42, available_coins))  # {25: 1, 10: 1, 5: 1, 1: 2}

available_coins = [25, 10, 1]  # Nickles out of stock
print(number_of_coins(42, available_coins))  # {25: 1, 10: 1, 1: 7}

available_coins = [25, 5, 1]  # Dimes out of stock
print(number_of_coins(42, available_coins))  # {25: 1, 10: 1, 5: 1, 1: 2}
