import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with (open(trades_file, "r") as file,
          open("profit.json", "w") as profit_file):
        actions = json.load(file)
        amount = 0
        profit = 0
        for action in actions:
            bought = Decimal(action["bought"]) if action["bought"] else 0
            sold = Decimal(action["sold"]) if action["sold"] else 0
            price = Decimal(action["matecoin_price"])
            amount += bought - sold
            profit += sold * price - bought * price
        json.dump(
            {
                "earned_money": str(profit),
                "matecoin_account": str(amount)
            },
            profit_file,
            indent=2
        )
