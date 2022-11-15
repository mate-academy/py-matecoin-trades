import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    bought, sold, bought_price, sold_price = 0, 0, 0, 0
    with open(trades_file, "r") as file:
        trades = json.load(file)
        for trade in trades:
            if trade["bought"] is not None:
                bought_price += Decimal(trade["bought"]) *\
                    Decimal(trade["matecoin_price"])
                bought += Decimal(trade["bought"])
            if trade["sold"] is not None:
                sold_price += Decimal(trade["sold"]) * \
                    Decimal(trade["matecoin_price"])
                sold += Decimal(trade["sold"])
        earned_money = sold_price - bought_price
        matecoin_account = bought - sold
        profit_dict = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
    with open("profit.json", "w") as file:
        json.dump(
            profit_dict,
            file,
            indent=2
        )
