import json

from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as f:
        data = json.load(f)

        earned_money = Decimal(0)
        matecoin_account = Decimal(0)

        for trade in data:
            bought = trade.get("bought")
            sold = trade.get("sold")
            matecoin_price = Decimal(trade["matecoin_price"])

            if bought:
                bought_amount = Decimal(bought)
                earned_money -= bought_amount * matecoin_price
                matecoin_account += bought_amount

            if sold:
                sold_amount = Decimal(sold)
                earned_money += sold_amount * matecoin_price
                matecoin_account -= sold_amount

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as output_file:
            json.dump(result, output_file, indent=2)
