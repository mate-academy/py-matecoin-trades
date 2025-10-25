import json
from decimal import Decimal
from typing import Dict, Any


def calculate_profit(trades_file: str) -> None:
    """
    Read trades from JSON file, calculate earned money and coin balance,
    then save the results into profit.json.
    """
    with open(trades_file, "r", encoding="utf-8") as trades_source:
        trades_data: list[Dict[str, Any]] = json.load(trades_source)

    earned_money: Decimal = Decimal("0")
    matecoin_account: Decimal = Decimal("0")

    for trade in trades_data:
        bought = (
            Decimal(trade["bought"]) if trade.get("bought") is not None else None
        )
        sold = (
            Decimal(trade["sold"]) if trade.get("sold") is not None else None
        )
        price = Decimal(trade["matecoin_price"])

        if bought is not None:
            matecoin_account += bought
            earned_money -= bought * price
        if sold is not None:
            matecoin_account -= sold
            earned_money += sold * price

    profit_data: Dict[str, str] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as profit_file:
        json.dump(profit_data, profit_file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
