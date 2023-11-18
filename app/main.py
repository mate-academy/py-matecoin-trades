import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open (file_name, "r") as file:
        trade_data = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trade_data:
        if trade["bought"] is not None:
            earned_money -= Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            matecoin_account += Decimal(trade["bought"])

        if trade["sold"] is not None:
            earned_money += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            matecoin_account -= Decimal(trade["sold"])

    temp_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(temp_dict, f, indent=2)
