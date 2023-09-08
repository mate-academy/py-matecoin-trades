import json
from decimal import Decimal
from typing import Any


def calculate_profit(input_file: Any) -> None:
    with open(input_file, "r") as f:
        trades_data = json.load(f)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trades_data:
        if trade["bought"] is not None:
            bought_volume = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money = earned_money - bought_volume * matecoin_price
            matecoin_account = matecoin_account + bought_volume
        if trade["sold"] is not None:
            sold_volume = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money = earned_money + sold_volume * matecoin_price
            matecoin_account = matecoin_account - sold_volume

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
