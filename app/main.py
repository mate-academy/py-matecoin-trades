import json
from decimal import Decimal


def calculate_profit(data_file: str) -> None:
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    with open(data_file) as file:
        data = json.load(file)

    for act in data:
        if act["bought"]:
            spend = Decimal(act["matecoin_price"]) * Decimal(act["bought"])
            matecoin_account += Decimal(act["bought"])
            earned_money -= spend
        if act["sold"]:
            earn = Decimal(act["matecoin_price"]) * Decimal(act["sold"])
            matecoin_account -= Decimal(act["sold"])
            earned_money += earn

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
