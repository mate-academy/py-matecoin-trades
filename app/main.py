import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = 0
    matecoin_account = 0
    trades = []

    with open(file_name, "r") as f:
        trades = json.load(f)

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        bought = trade.get("bought", 0)
        sold = trade.get("sold", 0)

        if bought:
            earned_money -= Decimal(bought) * matecoin_price
            matecoin_account += Decimal(bought)
        if sold:
            earned_money += Decimal(sold) * matecoin_price
            matecoin_account -= Decimal(sold)

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
