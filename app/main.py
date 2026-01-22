import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as f:
        trades = json.load(f)

    total_earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        bought_volume = (
            Decimal(trade["bought"])
            if trade["bought"] is not None
            else Decimal(0)
        )
        sold_volume = (
            Decimal(trade["sold"])
            if trade["sold"] is not None
            else Decimal(0)
        )
        matecoin_price = Decimal(trade["matecoin_price"])
        total_earned_money += (
            (sold_volume * matecoin_price)
            - (bought_volume * matecoin_price)
        )
        matecoin_account += bought_volume - sold_volume

    profit_data = {
        "earned_money": str(total_earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit_data, f, indent=2)
