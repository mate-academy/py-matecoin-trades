import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as f:
        trades_data = json.load(f)

    total_bought = Decimal("0")
    total_sold = Decimal("0")
    all_boughts = Decimal("0")
    all_solds = Decimal("0")

    for trade in trades_data:
        if trade["bought"]:
            all_boughts += Decimal(trade["bought"])
            total_bought += (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))

        if trade["sold"]:
            all_solds += Decimal(trade["sold"])
            total_sold += (Decimal(trade["sold"])
                           * Decimal(trade["matecoin_price"]))

    earned_money = (total_sold - total_bought)
    matecoin_account = all_boughts - all_solds

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
