import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "rb") as file_json:
        ls_data = json.load(file_json)

    matecoin_account = Decimal("0")
    earned_money = Decimal("0")
    for trade in ls_data:
        if trade["bought"]:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (
                Decimal(trade["matecoin_price"]) * Decimal(trade["bought"])
            )
        if trade["sold"]:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (
                Decimal(trade["matecoin_price"]) * Decimal(trade["sold"])
            )
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file_result:
        json.dump(result, file_result, indent=2)
