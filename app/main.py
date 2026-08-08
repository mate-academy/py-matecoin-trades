import json
import decimal


def calculate_profit(name: str) -> None:
    with open(name, "r") as f:
        data = json.load(f)

    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")
    for deal in data:
        price = decimal.Decimal(deal["matecoin_price"])
        if deal["sold"]:
            amount = decimal.Decimal(deal["sold"])
            earned_money += amount * price
            matecoin_account -= amount
        if deal["bought"]:
            amount = decimal.Decimal(deal["bought"])
            earned_money -= amount * price
            matecoin_account += amount

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
