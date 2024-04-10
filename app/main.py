import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    result = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    with open(file_name, "r") as file:
        trades = json.load(file)

        for transaction in trades:
            amount_bought = (Decimal(transaction["bought"])
                             if transaction["bought"] else Decimal("0"))
            amount_sold = (Decimal(transaction["sold"])
                           if transaction["sold"] else Decimal("0"))
            price = Decimal(transaction["matecoin_price"])

            result["earned_money"] += ((amount_sold * price)
                                       - (amount_bought * price))
            result["matecoin_account"] += (amount_bought - amount_sold)

    with open("profit.json", "w") as file:
        json.dump({k: str(v) for k, v in sorted(result.items())}, file, indent=2)

