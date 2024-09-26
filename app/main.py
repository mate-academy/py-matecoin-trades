import json

from _decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as data_in:
        trade_info = json.load(data_in)

    balance = 0
    matecoin_account = 0
    for transaction in trade_info:
        if transaction["bought"] is not None:
            balance -= Decimal(transaction["bought"]) * \
                Decimal(transaction["matecoin_price"])
            matecoin_account += Decimal(transaction["bought"])
        if transaction["sold"] is not None:
            balance += Decimal(transaction["sold"]) * \
                Decimal(transaction["matecoin_price"])
            matecoin_account -= Decimal(transaction["sold"])

    profit = {
        "earned_money": str(balance),
        "matecoin_account": str(matecoin_account),
    }
    with open("profit.json", "w") as data_out:
        json.dump(profit, data_out, indent=2)
