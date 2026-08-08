import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as json_file:
        data = json.load(json_file)

    new_list = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    for i in data:
        if i["bought"] is not None:
            bought = Decimal(i["bought"])
        else:
            bought = Decimal("0")
        if i["sold"] is not None:
            sold = Decimal(i["sold"])
        else:
            sold = Decimal("0")
        price = Decimal(i["matecoin_price"])

        new_list["earned_money"] += (sold - bought) * price
        new_list["matecoin_account"] += (bought - sold)

    new_list = {
        "earned_money": str(new_list["earned_money"]),
        "matecoin_account": str(new_list["matecoin_account"])
    }

    with open("profit.json", "w") as json_file:
        json.dump(new_list, json_file, indent=2)
