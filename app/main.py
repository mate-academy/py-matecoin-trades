import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    """
    Calculate profit from Matecoin trades and save results to profit.json.

    Args:
        file_name: Path to the JSON file containing trade information
    """
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        trade_bought = trade.get("bought")
        if trade_bought is not None:
            bought_volume = Decimal(trade_bought)
            matecoin_account += bought_volume
            earned_money -= bought_volume * matecoin_price

        trade_sold = trade.get("sold")
        if trade_sold is not None:
            sold_volume = Decimal(trade_sold)
            matecoin_account -= sold_volume
            earned_money += sold_volume * matecoin_price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
