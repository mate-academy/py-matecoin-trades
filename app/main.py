import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(name_file) as file:
        data = json.load(file)

    for operation in data:
        if operation["bought"]:
            earned_money -= (Decimal(operation["bought"])
                             * Decimal(operation["matecoin_price"]))
            matecoin_account += Decimal(operation["bought"])
        if operation["sold"]:
            earned_money += (Decimal(operation["sold"])
                             * Decimal(operation["matecoin_price"]))
            matecoin_account -= Decimal(operation["sold"])

    profit = {"earned_money": earned_money.to_eng_string(),
              "matecoin_account": matecoin_account.to_eng_string()}

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
