import json
from decimal import Decimal


def calculate_profit(json_file: str) -> None:
    earned_money = 0
    matecoin_account = 0
    with open(json_file, "r") as file:
        for item in json.load(file):
            if item["bought"]:
                earned_money -= Decimal(item.get("bought")) * Decimal(
                    item.get("matecoin_price")
                )
                matecoin_account += Decimal(item.get("bought"))
            if item["sold"]:
                earned_money += Decimal(item.get("sold")) * Decimal(
                    item.get("matecoin_price")
                )
                matecoin_account -= Decimal(item.get("sold"))

    with open("profit.json", "w") as profit_acc:
        json.dump(
            {
                "earned_money": str(f"{earned_money}"),
                "matecoin_account": str(matecoin_account),
            },
            profit_acc,
            indent=2,
        )
        print(profit_acc)
