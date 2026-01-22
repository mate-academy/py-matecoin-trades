from decimal import Decimal
import json


def calculate_profit(file_name):
    with open(file_name, "r") as f:
        python_data = json.load(f)

    money_profit = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for data in python_data:
        matecoin_price = Decimal(data["matecoin_price"])
        if data["bought"]:
            matecoin_account += Decimal(data["bought"])
            money_profit -= Decimal(data["bought"]) * matecoin_price
        if data["sold"]:
            matecoin_account -= Decimal(data["sold"])
            money_profit += Decimal(data["sold"]) * matecoin_price

    trade_result = {
        "money_profit": str(money_profit),
        "matecoin_account": str(matecoin_account)
    }

    print(trade_result)

    with open("profit.json", "w") as jsf:
        json.dump(trade_result, jsf, indent=2)
