import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as f:
        trades = json.load(f)

    total_bought = 0
    total_sold = 0
    total_amount_bought = 0
    total_amount_sold = 0
    for trade in trades:
        if trade["bought"] is not None:
            total_bought += Decimal(
                str(trade["bought"])) * Decimal(
                    str(trade["matecoin_price"]))
            total_amount_bought += Decimal(str(trade["bought"]))
        if trade["sold"] is not None:
            total_sold += Decimal(
                str(trade["sold"])) * Decimal(
                    str(trade["matecoin_price"]))
            total_amount_sold += Decimal(str(trade["sold"]))
    result = {"earned_money": str(total_sold - total_bought),
              "matecoin_account": str(total_amount_bought - total_amount_sold)}
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
