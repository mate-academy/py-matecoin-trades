
import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as f:
        trades_dict = json.load(f)

    total_bought = Decimal("0")
    total_sold = Decimal("0")
    matecoin_account = Decimal("0")

    for row in trades_dict:
        if row.get("bought") is not None:
            bought_amount = Decimal(row["bought"])
            matecoin_price = Decimal(row["matecoin_price"])

            total_bought += bought_amount * matecoin_price
            matecoin_account += bought_amount

    for row in trades_dict:
        if row.get("sold") is not None:
            sold_amount = Decimal(row["sold"])
            matecoin_price = Decimal(row["matecoin_price"])

            total_sold += sold_amount * matecoin_price
            matecoin_account -= sold_amount

    earned = total_sold - total_bought

    profit = {
        "earned_money": str(earned),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)

    return None
