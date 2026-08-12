import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with (
        open(file_name, "r") as file_to_read,
        open("profit.json", "w") as file_to_write,
    ):
        profit_info = json.load(file_to_read)
        earned_money = 0
        matecoin_account = 0

        for info in profit_info:
            sold_coins = Decimal(info.get("sold") or "0")
            bought_coins = Decimal(info.get("bought") or "0")
            price = Decimal(info.get("matecoin_price"))

            if bought_coins and sold_coins:
                matecoin_account += bought_coins - sold_coins
                earned_money += (sold_coins - bought_coins) * price
            elif sold_coins:
                earned_money += sold_coins * price
                matecoin_account -= sold_coins
            elif bought_coins:
                earned_money -= bought_coins * price
                matecoin_account += bought_coins

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }

        json.dump(result, file_to_write, indent=2)
