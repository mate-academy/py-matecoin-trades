import json
from decimal import Decimal


def calculate_profit(trade_info: str) -> None:
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)
    with open(trade_info, "r") as json_file:
        data = json.load(json_file)
    for transaction in data:
        if transaction["bought"]:
            matecoin_account += Decimal(transaction["bought"])
            earned_money -= (Decimal(transaction["bought"])
                             * Decimal(transaction["matecoin_price"]))
        if transaction["sold"]:
            matecoin_account -= Decimal(transaction["sold"])
            earned_money += (Decimal(transaction["sold"])
                             * Decimal(transaction["matecoin_price"]))
    new_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as json_file:
        json.dump(new_data, json_file, indent=2)
