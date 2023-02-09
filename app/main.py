import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file_out:
        operations = json.load(file_out)

    currency, bank = 0, 0

    for proc in operations:
        if proc["sold"] is None:
            proc["sold"] = 0
        if proc["bought"] is None:
            proc["bought"] = 0
        difference = (Decimal(proc["bought"]) - Decimal(proc["sold"]))
        bank -= difference * Decimal(proc["matecoin_price"])
        currency += difference

    profit_dict = {
        "earned_money": str(bank),
        "matecoin_account": str(currency)
    }

    with open("profit.json", "w") as file_in:
        json.dump(profit_dict, file_in, indent=2)
