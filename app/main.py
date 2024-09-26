import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        trade_data = json.load(f)

        coins = Decimal("0")
        total_profit = Decimal("0")

        for trade in trade_data:
            if trade["bought"] is not None:
                coins += Decimal(trade["bought"])
                total_profit -= Decimal(trade["bought"]) * Decimal(
                    trade["matecoin_price"]
                )
            if trade["sold"] is not None:
                coins -= Decimal(trade["sold"])
                total_profit += Decimal(trade["sold"]) * Decimal(
                    trade["matecoin_price"]
                )

        final_dict = (
            {"earned_money": str(total_profit),
             "matecoin_account": str(coins)}
        )
        with open("profit.json", "w") as f:
            json.dump(final_dict, f, indent=2)
