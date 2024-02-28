from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        price = Decimal(trade["matecoin_price"])

        if bought:
            matecoin_account += bought
            earned_money -= bought * price
        if sold:
            matecoin_account -= sold
            earned_money += sold * price

    result = {
        "earned_money": str(earned_money.normalize()),
        "matecoin_account": str(matecoin_account.normalize())
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
