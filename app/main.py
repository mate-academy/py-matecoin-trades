import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file_read:
        converting_file = json.load(file_read)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for action in converting_file:
        if action["bought"]:
            matecoin_account += Decimal(action.get("bought"))
            earned_money -= Decimal(action.get("bought")) * Decimal(
                action.get("matecoin_price")
            )
        if action["sold"]:
            matecoin_account -= Decimal(action.get("sold"))
            earned_money += Decimal(action.get("sold")) * Decimal(
                action.get("matecoin_price")
            )
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file_write:
        json.dump(result, file_write, indent=2)
