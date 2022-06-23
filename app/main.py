from decimal import Decimal
import json


def calculate_profit(file_name):
    with open(file_name) as f:
        data = json.load(f)
        earned = 0
        bought = 0
        coins_in_account = 0
        for i in data:
            if i["bought"]:
                coins_in_account += Decimal(i["bought"])
                bought += Decimal(i["bought"]) * Decimal(i["matecoin_price"])

                if i["sold"]:
                    earned += Decimal(i["sold"]) * Decimal(i["matecoin_price"])
                    coins_in_account -= Decimal(i["sold"])

            elif i["sold"]:
                coins_in_account -= Decimal(i["sold"])
                earned += Decimal(i["sold"]) * Decimal(i["matecoin_price"])

        with open("profit.json", "w") as prof:
            json.dump(
                {
                    "earned_money": f"{earned - bought}",
                    "matecoin_account": f"{coins_in_account}"
                },
                prof,
                indent=2
            )
