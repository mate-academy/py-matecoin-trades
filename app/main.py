import json
from decimal import Decimal
import os


def calculate_profit(file_name: str) -> None:
    data_account = {"earned_money": Decimal("0.00"), "matecoin_account": Decimal("0.00")}
    
    with open(file_name, "r") as file:
        transactions = json.load(file)

    for transaction in transactions:
        if transaction["bought"] is not None:
            data_account["matecoin_account"] += Decimal(transaction["bought"])
            data_account["earned_money"] -= Decimal(transaction["bought"]) * Decimal(transaction["matecoin_price"])
        if transaction["sold"] is not None:
            data_account["matecoin_account"] -= Decimal(transaction["sold"])
            data_account["earned_money"] += Decimal(transaction["sold"]) * Decimal(transaction["matecoin_price"])

    data_account["earned_money"] = str(data_account["earned_money"])
    data_account["matecoin_account"] = str(data_account["matecoin_account"])

    with open("profit.json", "w") as profit_file:
        json.dump(data_account, profit_file)


calculate_profit(os.path.join("app", "trades.json"))
