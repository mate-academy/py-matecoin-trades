import json
from decimal import Decimal


def calculate_profit(json_file: str) -> None:
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    with open(json_file, "r") as json_file:
        trade_data = json.load(json_file)
    for trade in trade_data:
        bought_solve_delta = Decimal(trade["bought"] or 0) - Decimal(trade["sold"] or 0)
        earned_money += -bought_solve_delta * Decimal(trade["matecoin_price"])
        matecoin_account += bought_solve_delta

    profit_json = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as json_file:
        json.dump(profit_json, json_file, indent=2)