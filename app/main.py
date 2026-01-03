import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    total_bought = Decimal("0")
    total_sold = Decimal("0")
    matecoin_account = Decimal("0")
    with open(file_name, "r") as file:
        trades = json.load(file)
    for trade in trades:
        if trade.get("bought") is not None:
            bought_volume = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            total_bought += bought_volume * matecoin_price
            matecoin_account += bought_volume

        if trade["sold"] is not None:
            sold_volume = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            total_sold += sold_volume * matecoin_price
            matecoin_account -= sold_volume
    profit = {"earned_money": str(total_sold - total_bought),
              "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
