import json
from decimal import Decimal


def calculate_profit(file_name: str):
    with open(file_name, "r") as file_in:
        list_of_trades = json.load(file_in)

    bought = 0
    sold = 0
    matecion_account = 0

    for transaction in list_of_trades:
        matecoin_price = Decimal(transaction["matecoin_price"])

        if transaction["bought"]:
            bought += Decimal(transaction["bought"]) * matecoin_price
            matecion_account += Decimal(transaction["bought"])

        if transaction["sold"]:
            sold += Decimal(transaction["sold"]) * matecoin_price
            matecion_account -= Decimal(transaction["sold"])

    profit_dict = {
        "earned_money": str(sold - bought),
        "matecoin_account": str(matecion_account)
    }

    with open("profit.json", "w") as file_out:
        json.dump(profit_dict, file_out, indent=2)
