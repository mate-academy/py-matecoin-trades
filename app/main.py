import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data = json.load(file)
    coin_balance = 0
    money_balance = 0
    for dictionary in data:
        if dictionary["bought"] is not None:
            coin_balance += Decimal(dictionary["bought"])
            money_balance -= (Decimal(dictionary["bought"])
                              * Decimal(dictionary["matecoin_price"]))
        if dictionary["sold"] is not None:
            coin_balance -= Decimal(dictionary["sold"])
            money_balance += (Decimal(dictionary["sold"])
                              * Decimal(dictionary["matecoin_price"]))

    result = {"earned_money": str(money_balance),
              "matecoin_account": str(coin_balance)}
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
