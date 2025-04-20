from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    with open(filename) as json_data, open("./profit.json", "w") as json_save:
        data = json.load(json_data)

        profit = Decimal(0)
        coins = Decimal(0)

        for block in data:
            if block["bought"] is not None:
                profit -= (Decimal(block["bought"])
                           * Decimal(block["matecoin_price"]))
                coins += Decimal(block["bought"])
            if block["sold"] is not None:
                profit += (Decimal(block["sold"])
                           * Decimal(block["matecoin_price"]))
                coins -= Decimal(block["sold"])

        json.dump(
            {
                "earned_money": str(profit),
                "matecoin_account": str(coins)
            },
            json_save,
            indent=2
        )
