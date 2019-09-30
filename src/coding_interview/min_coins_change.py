def number_of_coins(centes_in, coins):
    coins_dict = {}
    centes = centes_in
    for coin in coins:
        if coin <= centes:
            coins_dict[coin] = centes // coin
            centes = centes % coin
    return coins_dict


available_coins = [25, 10, 5, 1]
print(number_of_coins(42, available_coins))
