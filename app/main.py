import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades_data = json.load(f)

    total_coin_sold = Decimal("0")
    total_coin_bought = Decimal("0")

    total_bought = Decimal("0")
    total_sold = Decimal("0")

    for trade in trades_data:
        if trade["bought"] is not None:
            total_coin_bought += Decimal(trade["bought"])
            total_bought += (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))

        if trade["sold"] is not None:
            total_coin_sold += Decimal(trade["sold"])
            total_sold += (Decimal(trade["sold"])
                           * Decimal(trade["matecoin_price"]))

    matecoin_account = Decimal(total_coin_bought - total_coin_sold)
    earned_money = Decimal(total_sold - total_bought)

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit_data, profit_file, indent=2)
