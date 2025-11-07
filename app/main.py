import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        data: list = json.load(json_file)

    for item in data:
        for key in item:

            if item[key] is not None:
                item[key] = Decimal(item[key])

    data_of_trade = {
        "earned_money": Decimal(0),
        "matecoin_account": Decimal(0)
    }
    for item in data:

        bought = item["bought"]
        sold = item["sold"]
        matecoint_price = item["matecoin_price"]

        if bought is not None:
            data_of_trade["matecoin_account"] += bought
            data_of_trade["earned_money"] -= (bought * matecoint_price)

        if sold is not None:
            data_of_trade["matecoin_account"] -= sold
            data_of_trade["earned_money"] += (sold * matecoint_price)

    for key in data_of_trade:
        data_of_trade[key] = str(data_of_trade[key])

    with open("profit.json", "w") as profit_file:
        json.dump(data_of_trade, profit_file, indent=2)
