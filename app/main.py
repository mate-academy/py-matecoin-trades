from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as source_file:
        trades = json.load(source_file)

    profit = 0
    matecoin_account = 0
    for i in range(len(trades)):
        price = trades[i]["matecoin_price"]
        if trades[i]["bought"]:
            profit -= Decimal(trades[i]["bought"]) * Decimal(price)
            matecoin_account += Decimal(trades[i]["bought"])
        if trades[i]["sold"]:
            profit += Decimal(trades[i]["sold"]) * Decimal(price)
            matecoin_account -= Decimal(trades[i]["sold"])

    json_string = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as target_file:
        json.dump(json_string, target_file, indent=2)
