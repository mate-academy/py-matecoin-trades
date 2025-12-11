from decimal import Decimal, getcontext
import json

getcontext().prec = 28


def calculate_profit(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as file:
        trades_data = json.load(file)

        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for trade in trades_data:
            bought_str = trade["bought"]
            sold_str = trade["sold"]
            price_str = trade["matecoin_price"]

            price = Decimal(price_str)

            if bought_str is not None:
                bought = Decimal(bought_str)
                matecoin_account += bought
                earned_money -= price * bought

            if sold_str is not None:
                sold = Decimal(sold_str)
                matecoin_account -= sold
                earned_money += sold * price

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }

        with open("profit.json", "w", encoding="utf-8") as file:
            json.dump(result, file, indent=2)
