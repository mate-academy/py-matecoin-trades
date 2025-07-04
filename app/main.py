import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with (open(filename, "r") as f, open("profit.json", "w") as w):
        counter_coins, earned_money = Decimal(0), Decimal(0)
        data = json.load(f)
        for deal in data:
            if deal["bought"]:
                counter_coins += Decimal(deal["bought"])
                earned_money -= (Decimal(deal["bought"])
                                 * Decimal(deal["matecoin_price"]))
            if deal["sold"]:
                counter_coins -= Decimal(deal["sold"])
                earned_money += (Decimal(deal["sold"])
                                 * Decimal(deal["matecoin_price"]))
        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(counter_coins)
        }
        json.dump(result, w, indent=2)
