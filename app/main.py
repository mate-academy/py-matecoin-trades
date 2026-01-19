import json
from decimal import Decimal


def calculate_profit(trades_file_path: str) -> None:
    with open(trades_file_path, "rb") as input_file:
        trade_dicts = json.load(input_file)

    earned_money, matecoin_account = Decimal(0), Decimal(0)

    for trade_dict in trade_dicts:
        bought, sold, coin_price = trade_dict.values()
        try:
            coin_price = Decimal(coin_price)
            bought = Decimal(bought) if bought is not None else Decimal(0)
            sold = Decimal(sold) if sold is not None else Decimal(0)
        except ValueError as e:
            print(f"Invalid data in trades.json: {e}")
        earned_money += (sold - bought) * coin_price
        matecoin_account += bought - sold

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    try:
        with open("profit.json", "w") as output:
            json.dump(profit, output, indent=2)
        print("file was successfully saved")
    except IOError as e:
        print(f"{e}")
