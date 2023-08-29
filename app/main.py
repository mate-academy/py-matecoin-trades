import json
import decimal


def calculate_profit(filename: str = "trades.json") -> None:
    with open(filename) as f:
        trades_data = json.load(f)
        money = decimal.Decimal(0)
        coins = decimal.Decimal(0)
        for trade in trades_data:
            bought = (
                decimal.Decimal(trade["bought"])
                if trade["bought"] is not None
                else None
            )
            sold = (
                decimal.Decimal(trade["sold"])
                if trade["sold"] is not None
                else None
            )
            price = decimal.Decimal(trade["matecoin_price"])
            if bought is not None:
                money -= bought * price
                coins += bought
            if sold is not None:
                money += sold * price
                coins -= sold
    with open("../profit.json", "w") as f:
        money = str(money)
        coins = str(coins)
        data = {"earned_money": money, "matecoin_account": coins}
        json.dump(data, f, indent=2)


