import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data = json.load(file)

    money_profit = 0
    coins_on_account = 0

    for action in data:
        if action["bought"]:
            money_profit -= Decimal(action["bought"]
                                    ) * Decimal(action["matecoin_price"])
            coins_on_account += Decimal(action["bought"])

        if action["sold"]:
            money_profit += Decimal(action["sold"]
                                    ) * Decimal(action["matecoin_price"])
            coins_on_account -= Decimal(action["sold"])

    with open("profit.json", "w") as file:
        data = {"earned_money": str(money_profit),
                "matecoin_account": str(coins_on_account)}
        json.dump(data, file, indent=2)

    return None
