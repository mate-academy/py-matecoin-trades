import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    def to_decimal(value: str, default: str = "0.0") -> Decimal:
        return Decimal(default) if value is None else Decimal(value)
    with open(name, "r") as trades_file:
        data = json.load(trades_file)
        res = {"earned_money": 0, "matecoin_account": 0}
        for data in data:
            res["earned_money"] += (
                to_decimal(data["sold"]) - to_decimal(data["bought"])
            ) * to_decimal(data["matecoin_price"])
            res["matecoin_account"] += (
                to_decimal(data["bought"]) - to_decimal(data["sold"]))
        profit = {"earned_money": f"{res['earned_money']}",
                  "matecoin_account": f"{res['matecoin_account']}"}
        with open("profit.json", "w") as f:
            json.dump(profit, f, indent=2)
