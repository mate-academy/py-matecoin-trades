import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path) as trades_file:
        data = json.load(trades_file)
        earned_money = 0
        matecoin_account = 0
        for record in data:
            price = Decimal(record["matecoin_price"])
            if record["bought"] is not None:
                bought = Decimal(record["bought"])
                earned_money -= Decimal(bought) * Decimal(price)
                matecoin_account += Decimal(bought)

            if record["sold"] is not None:
                sold = Decimal(record["sold"])
                earned_money += Decimal(sold) * Decimal(price)
                matecoin_account -= Decimal(sold)

        profit_dict = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }

        with open("profit.json", "w") as profit_file:
            json.dump(profit_dict, profit_file, indent=2)
