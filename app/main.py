import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as source:
        trades = json.load(source)
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")
    for action in trades:
        if action["sold"] is None:
            action["sold"] = 0
        if action["bought"] is None:
            action["bought"] = 0
        bought = Decimal(action["bought"])
        sold = Decimal(action["sold"])
        matecoin_account += bought - sold
        earned_money += (sold - bought) * Decimal(action["matecoin_price"])
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as profit:
        json.dump(result, profit, indent=2)
