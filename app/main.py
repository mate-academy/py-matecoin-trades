import json
from decimal import Decimal


def calculate_profit(trades_file_path: str) -> None:
    with open(trades_file_path, "rb") as input_file:
        trades_dicts = json.load(input_file)

    earned_money, matecoin_account = Decimal(0), Decimal(0)

    for trades_dict in trades_dicts:
        bought, sold, coin_price = trades_dict.values()

        coin_price = Decimal(coin_price)

        bought = Decimal(bought) if bought is not None else Decimal(0)
        sold = Decimal(sold) if sold is not None else Decimal(0)

        earned_money += (sold - bought) * coin_price
        matecoin_account += bought - sold

    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as output_file:
        json.dump(profit_dict, output_file, indent=2)
