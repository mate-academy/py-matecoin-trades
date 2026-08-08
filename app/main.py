import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as out_file, open(
        "profit.json", "w"
    ) as input_file:
        info = {"earned_money": 0, "matecoin_account": 0}
        trades_info = json.load(out_file)
        for transaction in trades_info:
            if transaction["bought"]:
                info["earned_money"] -= Decimal(
                    transaction["bought"]
                ) * Decimal(transaction["matecoin_price"])
                info["matecoin_account"] += Decimal(transaction["bought"])
            if transaction["sold"]:
                info["earned_money"] += Decimal(transaction["sold"]) * Decimal(
                    transaction["matecoin_price"]
                )
                info["matecoin_account"] -= Decimal(transaction["sold"])
        info = {key: str(value) for key, value in info.items()}
        json.dump(info, input_file, indent=2)
