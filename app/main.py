import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trade_information = json.load(file)
    profit = {"earned_money": 0,
              "matecoin_account": 0}
    for transaction in trade_information:
        if transaction["bought"] is None:
            transaction["bought"] = 0
        if transaction["sold"] is None:
            transaction["sold"] = 0
        bought = Decimal(f"{transaction['bought']}")
        matecoin_price = Decimal(f"{transaction['matecoin_price']}")
        sold = Decimal(f"{transaction['sold']}")
        profit["earned_money"] += ((sold * matecoin_price)
                                   - (bought * matecoin_price))
        profit["matecoin_account"] += bought - sold

    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
