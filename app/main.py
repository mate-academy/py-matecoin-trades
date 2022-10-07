import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        data = json.load(file)

        sold, bouth, coins = 0, 0, 0

        for day in data:
            day_price = Decimal(day["matecoin_price"])
            if day["bought"]:
                bouth += Decimal(day["bought"]) * day_price
                coins += Decimal(day["bought"])
            if day["sold"]:
                sold += Decimal(day["sold"]) * day_price
                coins -= Decimal(day["sold"])

            result = {"earned_money": str(sold - bouth),
                      "matecoin_account": str(coins)}

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
