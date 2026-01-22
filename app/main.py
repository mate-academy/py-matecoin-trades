import json
from decimal import Decimal


class Trade:
    def __init__(self, coins: Decimal, money: Decimal) -> None:
        self.coins = coins
        self.money = money

    def buy(self, coins_quantity: float, coin_price: float) -> None:
        self.coins += Decimal(coins_quantity)
        self.money -= Decimal(coin_price) * Decimal(coins_quantity)

    def sell(self, coins_quantity: Decimal, coin_price: Decimal) -> None:
        self.coins -= Decimal(coins_quantity)
        self.money += Decimal(coin_price) * Decimal(coins_quantity)


def calculate_profit(
    file_name: str,
) -> None:
    wallet = Trade(Decimal(str(0)), Decimal(str(0)))

    with open(file_name, "r") as trades:
        trades_data = json.load(trades)
        for trade in trades_data:
            if trade["bought"]:
                wallet.buy(trade.get("bought"), trade.get("matecoin_price"))

            if trade["sold"]:
                wallet.sell(trade.get("sold"), trade.get("matecoin_price"))

    with open("profit.json", "w") as trade_profit:
        json.dump(
            {"earned_money": str(wallet.money),
             "matecoin_account": str(wallet.coins)},
            trade_profit,
            indent=2,
        )
