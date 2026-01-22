import json
from decimal import Decimal


def calculate_profit(trades: list) -> None:
    with open(f"{trades}", "r") as f:
        list_trades_description = json.load(f)
    sold, bought, sold_sum, bought_sum = 0, 0, 0, 0
    for trade in list_trades_description:
        if trade["bought"] is not None:
            bought += Decimal(trade["bought"])
            bought_sum += Decimal(trade["bought"]) * \
                Decimal(trade["matecoin_price"])
        if trade["sold"] is not None:
            sold += Decimal(trade["sold"])
            sold_sum += Decimal(trade["sold"]) * \
                Decimal(trade["matecoin_price"])

    profit_dict = {
        "earned_money": str(sold_sum - bought_sum),
        "matecoin_account": str(bought - sold)
    }

    with open("profit.json", "w") as f:
        json.dump(profit_dict, f, indent=2)
