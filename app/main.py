import json

from decimal import Decimal


def calculate_profit(filename: str) -> None:

    with open(filename, "r") as f:
        trade_data = json.load(f)

    earned_money, matecoin_account = Decimal("0"), Decimal("0")
    for i in trade_data:
        if i["bought"]:
            earned_money -= Decimal(i["bought"]) * Decimal(i["matecoin_price"])
            matecoin_account += Decimal(i["bought"])
        if i["sold"]:
            earned_money += Decimal(i["sold"]) * Decimal(i["matecoin_price"])
            matecoin_account -= Decimal(i["sold"])

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit_data, f, indent=2)
