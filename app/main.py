import json
from _decimal import Decimal


def calculate_profit(file_name: str) -> None:
    dollar = 0
    account = 0
    with (open(file_name, "r") as file_of_transaction,
          open("profit.json", "w") as file_of_profit):
        transactions = json.load(file_of_transaction)

        for transaction in transactions:
            if transaction["bought"]:
                dollar -= (Decimal(transaction["bought"])
                           * Decimal(transaction["matecoin_price"]))
                account += Decimal(transaction["bought"])
            if transaction["sold"]:
                dollar += (Decimal(transaction["sold"])
                           * Decimal(transaction["matecoin_price"]))
                account -= Decimal(transaction["sold"])

        json.dump({"earned_money": str(dollar),
                   "matecoin_account": str(account)},
                  file_of_profit,
                  indent=2)
