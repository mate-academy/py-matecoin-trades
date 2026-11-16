import json
from decimal import Decimal

PROFIT_FILE_NAME = "profit.json"


def calculate_profit(trades_file_name: str) -> None:
    with open(trades_file_name) as trades_file:
        trades = json.load(trades_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_volume = Decimal(trade["bought"])
            matecoin_account += bought_volume
            earned_money -= bought_volume * price

        if trade["sold"] is not None:
            sold_volume = Decimal(trade["sold"])
            matecoin_account -= sold_volume
            earned_money += sold_volume * price

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open(PROFIT_FILE_NAME, "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
