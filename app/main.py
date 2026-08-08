import json
from decimal import Decimal

FILE_DESTINATION = "profit.json"


def calculate_profit(file_source: str) -> None:
    money_profit = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    with open(file_source, "r") as file_obj:
        operations = json.load(file_obj)

    for action in operations:
        if action["bought"]:
            matecoin_account += Decimal(action["bought"])
            money_profit -= (Decimal(action["bought"])
                             * Decimal(action["matecoin_price"]))
        if action["sold"]:
            matecoin_account -= Decimal(action["sold"])
            money_profit += (Decimal(action["sold"])
                             * Decimal(action["matecoin_price"]))

    with open(FILE_DESTINATION, "w") as file_obj:
        json.dump({
            "earned_money": str(money_profit),
            "matecoin_account": str(matecoin_account)
        }, file_obj, indent=2)
