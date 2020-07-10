class CoinDispenser:
    def __init__(self, coins):
        self.coins = sorted(coins, reverse=True)

    def dispense(self, amount):
        dispensable_amount = 0
        coin_count = 0

        for coin in self.coins:
            if ((amount - dispensable_amount) // coin) == 0:
                continue

            coin_count += (amount-dispensable_amount) // coin
            dispensable_amount += ((amount-dispensable_amount) // coin) * coin

        return coin_count if dispensable_amount == amount else -1