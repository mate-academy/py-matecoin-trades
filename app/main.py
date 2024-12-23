import json
from decimal import Decimal


def calculate_profit(input_file: str = "trades.json",
                     output_file: str = "profit.json") -> None:
    with open(input_file, "r") as trades_file:
        trades = json.load(trades_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade.get("bought") or "0")
        sold = Decimal(trade.get("sold") or "0")
        matecoin_price = Decimal(trade["matecoin_price"])

        earned_money += sold * matecoin_price - bought * matecoin_price

        matecoin_account += bought - sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(output_file, "w") as profit_file:
        json.dump(result, profit_file, indent=2)
