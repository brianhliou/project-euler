def coin_sum(coins, target):
    if target == 0:
        return 1
    if target < 0:
        return 0
    if len(coins) == 0:
        return 0
    return coin_sum(coins, target - coins[0]) + coin_sum(coins[1:], target)

if __name__ == '__main__':
    print(coin_sum([1, 2, 5, 10, 20, 50, 100, 200], 200))
    