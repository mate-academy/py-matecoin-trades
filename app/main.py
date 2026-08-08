import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0")
    account_status = Decimal("0")

    with open(f"{filename}", "r") as f:
        trades = json.load(f)

        for transaction in trades:
            if transaction["bought"]:
                account_status += Decimal(transaction["bought"])
                earned_money -= (Decimal(transaction["bought"])
                                 * Decimal(transaction["matecoin_price"]))
            if transaction["sold"]:
                account_status -= Decimal(transaction["sold"])
                earned_money += (Decimal(transaction["sold"])
                                 * Decimal(transaction["matecoin_price"]))
        profit = {
            "earned_money": f"{earned_money}",
            "matecoin_account": f"{account_status}"
        }

        with open("profit.json", "w") as result:
            json.dump(profit, result, indent=2)
