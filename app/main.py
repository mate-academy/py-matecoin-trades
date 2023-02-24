from decimal import Decimal
import json


def calculate_profit(trades_file_name: str,
                     profit_file_name: str = None) -> None:
    with open(trades_file_name, "r") as f:
        trades = json.load(f)

    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * Decimal(trade["matecoin_price"])
        elif trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * Decimal(trade["matecoin_price"])

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    if profit_file_name is not None:
        with open(profit_file_name, "w") as f:
            json.dump(result, f)

    return None
