from decimal import Decimal
import json
import os


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        data = json.load(f)

    current_money_balance = Decimal(0)
    current_coin_balance = Decimal(0)

    for trade in data:
        if trade["bought"] is not None:
            current_coin_balance += Decimal(trade["bought"])
            current_money_balance -= (
                Decimal(trade["bought"])
                * Decimal(trade["matecoin_price"])
            )

        if trade["sold"] is not None:
            current_coin_balance -= Decimal(trade["sold"])
            current_money_balance += (
                Decimal(trade["sold"])
                * Decimal(trade["matecoin_price"])
            )

    final_balance = {
        "earned_money": str(current_money_balance),
        "matecoin_account": str(current_coin_balance),
    }

    project_dir = os.path.dirname(os.path.dirname(file_name))
    profit_path = os.path.join(project_dir, "profit.json")

    with open(profit_path, "w") as f:
        json.dump(final_balance, f, indent=2)
