import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as origin, open("profit.json", "w") as new:
        data = json.load(origin)
        bought = 0
        sold = 0
        bought_matecoin = 0
        sold_matecoin = 0
        for obj in data:
            current_price = decimal.Decimal(obj["matecoin_price"])
            if obj["bought"] is not None:
                bought += decimal.Decimal(obj["bought"])
                bought_matecoin += decimal.Decimal(obj["bought"]) \
                    * current_price
            if obj["sold"] is not None:
                sold += decimal.Decimal(obj["sold"])
                sold_matecoin += decimal.Decimal(obj["sold"]) * current_price
        earned_money = str(sold_matecoin - bought_matecoin)
        matecoin_account = str(bought - sold)
        profit = {
            "earned_money": earned_money,
            "matecoin_account": matecoin_account
        }
        json.dump(profit, new, indent=2)
