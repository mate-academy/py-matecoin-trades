import json
from decimal import Decimal


def calculate_profit(name_of_the_file: str) -> None:
    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")
    with open(name_of_the_file, "r") as file_to_read:
        json_trades = json.load(file_to_read)
    for operation in json_trades:
        if operation["bought"] is not None:
            matecoin_account += Decimal(operation["bought"])
            earned_money -= (Decimal(operation["bought"])
                             * Decimal(operation["matecoin_price"]))
        if operation["sold"] is not None:
            matecoin_account -= Decimal(operation["sold"])
            earned_money += (Decimal(operation["sold"])
                             * Decimal(operation["matecoin_price"]))
    result = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as profit:
        profit = json.dump(result, profit, indent=2)
