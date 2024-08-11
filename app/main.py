# write your code here
import json
from decimal import Decimal


def calculate_profit(trade: str) -> None:
    result = {"earned_money": Decimal("0.0"),
              "matecoin_account": Decimal("0.0")}

    with open(trade, "r") as f:
        trades = json.load(f)

        for trade in trades:
            if trade["bought"]:
                result["earned_money"] -= (
                    Decimal(trade["matecoin_price"]) * Decimal(trade["bought"])
                )
                result["matecoin_account"] += Decimal(trade["bought"])
            if trade["sold"]:
                result["earned_money"] += (
                    Decimal(trade["matecoin_price"]) * Decimal(trade["sold"])
                )
                result["matecoin_account"] -= Decimal(trade["sold"])

    result = {"earned_money": str(result["earned_money"]),
              "matecoin_account": str(result["matecoin_account"])}

    with open("profit.json", "w") as profit:
        json.dump(result, profit, indent=2)
