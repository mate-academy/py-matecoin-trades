import json
import decimal


def calculate_profit(name: str) -> None:
    with open(name, "r") as file:
        trades = json.load(file)

    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    for trade in trades:
        price = decimal.Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            amount = decimal.Decimal(trade["bought"])
            earned_money -= amount * price
            matecoin_account += amount

        if trade["sold"] is not None:
            amount = decimal.Decimal(trade["sold"])
            earned_money += amount * price
            matecoin_account -= amount

    result = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
