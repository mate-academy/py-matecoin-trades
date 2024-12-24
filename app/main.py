import json
from decimal import Decimal


def calculate_profit(trades_file_path: str) -> None:
    with open(trades_file_path, "rb") as input_file:
        trades_dicts = json.load(input_file)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trades_dict in trades_dicts:
        coin_price = Decimal(trades_dict["matecoin_price"])

        bought = trades_dict["bought"]
        if bought is not None:
            bought = Decimal(bought)
        else:
            bought = Decimal(0)

        sold = trades_dict["sold"]
        if sold is not None:
            sold = Decimal(sold)
        else:
            sold = Decimal(0)

        earned_money += (sold * coin_price) - (bought * coin_price)
        matecoin_account += bought - sold

    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as output_file:
        json.dump(profit_dict, output_file, indent=2)
