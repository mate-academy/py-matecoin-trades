import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as file:
        trades_data = json.load(file)

    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    for trade in trades_data:
        coins_i_bought = Decimal(trade.get("bought")) \
            if trade.get("bought") is not None else Decimal(0)
        coins_i_sold = Decimal(trade.get("sold")) \
            if trade.get("sold") is not None else Decimal(0)
        coins_i_mate = Decimal(trade.get("matecoin_price"))

        if coins_i_bought:
            earned_money -= coins_i_bought * coins_i_mate
            matecoin_account += coins_i_bought
        if coins_i_sold:
            earned_money += coins_i_sold * coins_i_mate
            matecoin_account -= coins_i_sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as output_file:
        json.dump(result, output_file)
