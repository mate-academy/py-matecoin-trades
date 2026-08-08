import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades_dict = json.load(f)

    all_bought = 0
    all_sold = 0
    money_b = 0
    money_s = 0

    for trade in trades_dict:
        for key, value in trade.items():
            if key == "bought" and value is not None:
                all_bought += Decimal(value)
                money_b += Decimal(value) * Decimal(trade["matecoin_price"])
            if key == "sold" and value is not None:
                all_sold += Decimal(value)
                money_s += Decimal(value) * Decimal(trade["matecoin_price"])

    earned_money = money_s - money_b
    matecoin_account = all_bought - all_sold

    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit_dict, f, indent=2)
