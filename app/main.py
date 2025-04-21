import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:

    result = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    with open(filename, "r") as data_file:
        trades_data = json.load(data_file)

    bought_coins = Decimal("0")
    sold_coins = Decimal("0")
    bought_sum = Decimal("0")
    sold_sum = Decimal("0")
    for trade in trades_data:
        if trade["bought"] is not None:
            bought_sum += (Decimal(
                f'{trade["bought"]}') * Decimal(
                f'{trade["matecoin_price"]}'))
            bought_coins += Decimal(f'{trade["bought"]}')
        if trade["sold"] is not None:
            sold_sum += (Decimal(
                f'{trade["sold"]}') * Decimal(
                f'{trade["matecoin_price"]}'))
            sold_coins += Decimal(f'{trade["sold"]}')

    result["earned_money"] = str(sold_sum - bought_sum)
    result["matecoin_account"] = str(bought_coins - sold_coins)

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
