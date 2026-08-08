import json

from decimal import Decimal


def calculate_profit(name: str) -> None:
    with open(name, "r") as file:
        trades_dict = json.load(file)
    profit_dict = {
        "earned_money": "0",
        "matecoin_account": "0"
    }
    for operation in trades_dict:
        for key in operation:
            if key == "bought" and operation["bought"]:
                profit_dict["earned_money"] = str(
                    Decimal(profit_dict["earned_money"]) - (
                        Decimal(operation["bought"])
                        * Decimal(operation["matecoin_price"])
                    )
                )
                profit_dict["matecoin_account"] = str(
                    Decimal(profit_dict["matecoin_account"])
                    + Decimal(operation["bought"])
                )
            elif key == "sold" and operation["sold"]:
                profit_dict["earned_money"] = str(
                    Decimal(profit_dict["earned_money"]) + (
                        Decimal(operation["sold"])
                        * Decimal(operation["matecoin_price"])
                    )
                )
                profit_dict["matecoin_account"] = str(
                    Decimal(profit_dict["matecoin_account"])
                    - Decimal(operation["sold"])
                )
    with open("profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2)
