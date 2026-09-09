import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as f:
        data = json.load(f)
        matecoin_account = Decimal("0")
        earned_money = Decimal("0")
        for trade in data:
            bought = trade["bought"]
            sold = trade["sold"]
            price = Decimal(trade["matecoin_price"])
            if bought:
                qty = Decimal(bought)
                matecoin_account += qty
                earned_money -= qty * price
            if sold:
                qty = Decimal(sold)
                matecoin_account -= qty
                earned_money += qty * price

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        with open("profit.json", "w") as f:
            json.dump(result, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
