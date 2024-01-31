import json
from decimal import Decimal
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def calculate_profit(trades_file: list) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    result_bought = Decimal(0)
    result_bought_price = Decimal(0)

    result_sold = Decimal(0)
    result_sold_price = Decimal(0)

    for trade in trades:
        if trade["bought"] is not None:
            bought_amount = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            bought_price = matecoin_price
            bought = bought_amount
            result_bought += bought * bought_price
            result_bought_price += bought

        if trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            sold_price = matecoin_price
            sold = sold_amount
            result_sold += sold * sold_price
            result_sold_price += sold

    earned_money = result_sold - result_bought
    matecoin_account = result_bought_price - result_sold_price

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(f"{BASE_DIR}/profit.json", "w") as output_file:
        json.dump(profit_data, output_file, indent=2)
