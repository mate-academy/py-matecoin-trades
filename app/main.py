import json

from decimal import Decimal


def calculate_profit(information_file: str) -> None:
    with open(information_file) as j:
        information_dict = json.load(j)
    total_amount = Decimal("0")
    matecoin_account = Decimal("0")
    for account in information_dict:
        if account["sold"] is not None:
            total_amount += (Decimal(account["sold"])
                             * Decimal(account["matecoin_price"]))
            matecoin_account -= Decimal(account["sold"])
        if account["bought"] is not None:
            total_amount -= (Decimal(account["bought"])
                             * Decimal(account["matecoin_price"]))
            matecoin_account += Decimal(account["bought"])

    profit_file = {
        "earned_money": str(total_amount),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as json_file:
        json.dump(profit_file, json_file, indent=2)
