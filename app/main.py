import decimal
import json


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        data = json.load(f)

    earned_money = decimal.Decimal(0)
    matecoin_account = decimal.Decimal(0)

    for i in data:
        prise = decimal.Decimal(i["matecoin_price"])
        if i["sold"]:
            amount = decimal.Decimal(i["sold"])
            earned_money += amount * prise
            matecoin_account -= amount
        if i["bought"]:
            amount = decimal.Decimal(i["bought"])
            earned_money -= amount * prise
            matecoin_account += amount

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
