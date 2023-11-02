

def minCoins(coins, finalAmount):
    #list to store the minimum number of coins for each amount from 0 to the target amount.
    
    list = [float('inf')] * (finalAmount + 1)
    list[0] = 0 #set the value at the first index of the list to 0

    
    for coin in coins: # iterates through each coin denomination in the coins list
        for amount in range(coin, finalAmount + 1): #iterates through each possible amount from the coin's value (coin) up to the finalAmount
            if list[amount - coin] + 1 < list[amount]:  #If using the current coin results in a smaller number of coins needed, the code updates list[amount] with that smaller value
                list[amount] = list[amount - coin] + 1

    # value at list[finalAmount] will be the minimum number of coins needed
    return list[finalAmount]

#coin denominations
coins = [100, 200, 500]
finalAmount = 29100

# Call the function
minCoinsoins1 = minCoins(coins, finalAmount)
print(f"It takes {minCoinsoins1} coins to make {finalAmount}")
