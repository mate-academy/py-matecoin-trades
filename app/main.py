import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file_read:
        transactions_list = json.load(file_read)
    total_profit = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }
    for transaction in transactions_list:
        if transaction["bought"] is not None:
            amount = Decimal(str(transaction["bought"]))
            price = Decimal(str(transaction["matecoin_price"]))
            total_profit["earned_money"] -= amount * price
            total_profit["matecoin_account"] += amount
        if transaction["sold"] is not None:
            amount = Decimal(str(transaction["sold"]))
            price = Decimal(str(transaction["matecoin_price"]))
            if total_profit["matecoin_account"] >= amount:
                total_profit["earned_money"] += amount * price
                total_profit["matecoin_account"] -= amount
    total_profit["earned_money"] = str(total_profit["earned_money"])
    total_profit["matecoin_account"] = str(total_profit["matecoin_account"])
    with open("profit.json", "w") as file_write:
        json.dump(total_profit, file_write, indent=2)
