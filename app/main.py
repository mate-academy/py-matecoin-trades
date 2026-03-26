import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        conv_dict = json.load(file)

    money_balance = Decimal("0")
    coin_balance = Decimal("0")

    for data in conv_dict:
        if data["bought"] is not None:
            money_balance -= (
                    Decimal(data["bought"])
                    * Decimal(data["matecoin_price"])
            )
            coin_balance += Decimal(data["bought"])

        if data["sold"] is not None:
            money_balance += (
                    Decimal(data["sold"])
                    * Decimal(data["matecoin_price"])
            )
            coin_balance -= Decimal(data["sold"])

    bank = {
        "earned_money": str(money_balance),
        "matecoin_account": str(coin_balance),
    }

    with open("profit.json", "w") as file:
        json.dump(bank, file, indent=2)
