from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)
    amount_of_coin = Decimal("0.0")
    money_balance = Decimal("0.0")
    for trade in trades:
        if trade["bought"] is not None:
            amount_of_coin += Decimal(trade["bought"])
            money_balance -= (
                    Decimal(trade["matecoin_price"])
                    * Decimal(trade["bought"])
                )
        if trade["sold"] is not None:
            amount_of_coin -= Decimal(trade["sold"])
            money_balance += (
                    Decimal(trade["matecoin_price"])
                    * Decimal(trade["sold"])
                )
    res = {
        "earned_money": str(money_balance),
        "matecoin_account": str(amount_of_coin),
    }
    with open("profit.json", "w") as f:
        json.dump(res, f, indent=2)
