import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        if trade["matecoin_price"]:
            price = Decimal(trade["matecoin_price"])
        else:
            price = Decimal("0")

        matecoin_account += bought
        earned_money -= bought * price

        matecoin_account -= sold
        earned_money += sold * price

    earned_money = earned_money.normalize()
    matecoin_account = matecoin_account.normalize()

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as json_file:
        json.dump(profit_data, json_file, indent=2)

# if __name__ == "__main__":
#     calculate_profit()
