from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file_read, open("profit.json", "w") as file_write:
        context = json.load(file_read)

        coins = []
        money = []
        for day in context:
            if day["sold"] is None:
                day["sold"] = 0
            if day["bought"] is None:
                day["bought"] = 0

            if Decimal(day["sold"]) > Decimal(day["bought"]):
                day["sold"] = Decimal(day["sold"]) - Decimal(day["bought"])
                day["bought"] = 0
            else:
                day["bought"] = Decimal(day["bought"]) - Decimal(day["sold"])
                day["sold"] = 0

            if day["bought"] != 0:
                coins.append(Decimal(day["bought"]))
                money.append(
                    -(Decimal(day["bought"]) * Decimal(day["matecoin_price"]))
                )

            if day["sold"] != 0:
                coins.append(Decimal(-day["sold"]))

                money.append(
                    Decimal(day["sold"]) * Decimal(day["matecoin_price"])
                )
        information = {
            "earned_money": str(sum(money)),
            "matecoin_account": str(sum(coins)),
        }

        json.dump(information, file_write, indent=2)
