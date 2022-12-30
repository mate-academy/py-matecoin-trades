import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = 0
    matecoin_account = 0
    with open(file_name, "r") as trades_file:
        convert_file = json.load(trades_file)
    for operation in convert_file:
        if operation["bought"]:
            earned_money -= (Decimal(operation["bought"])
                             * Decimal(operation["matecoin_price"]))
            matecoin_account += Decimal(operation["bought"])
        if operation["sold"]:
            earned_money += (Decimal(operation["sold"])
                             * Decimal(operation["matecoin_price"]))
            matecoin_account -= Decimal(operation["sold"])
    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as profit_file:
        json.dump(profit_dict, profit_file, indent=2)
