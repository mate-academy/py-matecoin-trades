from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades_json = json.load(f)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for char in trades_json:
        price = Decimal(char["matecoin_price"])
        if char["bought"] is not None:
            bought = Decimal(char["bought"])
            earned_money -= bought * price
            matecoin_account += bought
        if char["sold"] is not None:
            sold = Decimal(char["sold"])
            earned_money += sold * price
            matecoin_account -= sold
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
