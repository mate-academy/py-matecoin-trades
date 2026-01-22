import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        json_list = json.load(file)
        total = Decimal("0")
        matecoin_account = Decimal("0")
        for element in json_list:
            if element["bought"]:
                total -= Decimal(element["bought"]
                                 ) * Decimal(element["matecoin_price"])
                matecoin_account += Decimal(element["bought"])
            if element["sold"]:
                total += Decimal(element["sold"]
                                 ) * Decimal(element["matecoin_price"])
                matecoin_account -= Decimal(element["sold"])
        result = {"earned_money": str(total),
                  "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
