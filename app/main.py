import json
from decimal import Decimal
from typing import List, Union

Trade = dict[str, Union[str, None]]


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as f:
        trades_data: List[Trade] = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_volume = Decimal(trade["bought"])
            cost = matecoin_price * bought_volume
            matecoin_account += bought_volume
            earned_money -= cost

        if trade["sold"] is not None:
            sold_volume = Decimal(trade["sold"])
            earning = matecoin_price * sold_volume
            matecoin_account -= sold_volume
            earned_money += earning

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
