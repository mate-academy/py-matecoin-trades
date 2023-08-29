from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    totally_sold = Decimal(0)
    totally_bought = Decimal(0)
    wallet_count = Decimal(0)
    with open(file_name, "r") as file:
        transactions = json.load(file)
    for transaction in transactions:
        if transaction.get("bought"):
            totally_bought += (Decimal(transaction["bought"])
                               * Decimal(transaction["matecoin_price"]))
            wallet_count += Decimal(transaction["bought"])
        if transaction.get("sold"):
            totally_sold += (Decimal(transaction["sold"])
                             * Decimal(transaction["matecoin_price"]))
            wallet_count -= Decimal(transaction["sold"])
    wallet_info = {
        "earned_money": str(totally_sold - totally_bought),
        "matecoin_account": str(wallet_count),
    }
    with open("profit.json", "w") as file:
        json.dump(wallet_info, file, indent=2)
