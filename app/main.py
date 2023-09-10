import json
from decimal import Decimal


def calculate_profit(json_file: str) -> None:
    result = Decimal(0)
    coins = Decimal(0)

    with open(json_file, "r") as file:
        trade_data = json.load(file)

    for elem in trade_data:
        if elem["bought"]:
            result -= \
                (Decimal(elem["bought"]) * Decimal(elem["matecoin_price"]))
            coins += Decimal(elem["bought"])

        if elem["sold"]:
            result += (Decimal(elem["sold"]) * Decimal(elem["matecoin_price"]))
            coins -= Decimal(elem["sold"])

    output_date = {"earned_money": result, "matecoin_account": coins}
    output_date = json.dumps(output_date)

    with open("profit.json", "w") as f:
        json.dump(output_date, f)
