import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as operations:
        transactions = json.load(operations)
        bought = 0
        sold = 0
        matecoin_account = 0
        for action in transactions:
            if action["bought"]:
                bought += (Decimal(action["bought"])
                           * Decimal(action["matecoin_price"]))
                matecoin_account += Decimal(action["bought"])
            if action["sold"]:
                sold += (Decimal(action["sold"])
                         * Decimal(action["matecoin_price"]))
                matecoin_account -= Decimal(action["sold"])
        account = {
            "earned_money": str(sold - bought),
            "matecoin_account": str(matecoin_account)
        }
    with open("profit.json", "w") as result:
        json.dump(account, result, indent=2)
