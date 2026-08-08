from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    coins_count = Decimal()
    money_spent = Decimal()
    money_earned = Decimal()
    with open(file_name, "r") as data_in, open("profit.json", "w") as profit:
        days_info = json.load(data_in)
        for day in days_info:
            if day["bought"] is not None:
                coins_count += Decimal(day["bought"])
                money_spent += \
                    Decimal(day["bought"]) * Decimal(day["matecoin_price"])
            if day["sold"] is not None:
                coins_count -= Decimal(day["sold"])
                money_earned += \
                    Decimal(day["sold"]) * Decimal(day["matecoin_price"])
        result_profit = {
            "earned_money": str(money_earned - money_spent),
            "matecoin_account": str(coins_count)
        }
        json.dump(result_profit, profit, indent=2, sort_keys=True)
