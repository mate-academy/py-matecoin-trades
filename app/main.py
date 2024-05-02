import json
from decimal import Decimal


def calculate_profit(file_json: json) -> None:
    with open(file_json) as trades_file:
        trades_info = json.load(trades_file)

    profit = {"earned_money": Decimal("0"), "matecoin_account": Decimal("0")}

    for transaction in trades_info:
        if transaction["sold"]:
            profit["matecoin_account"] -= Decimal(str(transaction["sold"]))
            profit["earned_money"] \
                += (Decimal(str(transaction["sold"]))
                    * Decimal(str(transaction["matecoin_price"])))
        if transaction["bought"]:
            profit["matecoin_account"] += Decimal(str(transaction["bought"]))
            profit["earned_money"] \
                -= (Decimal(str(transaction["bought"]))
                    * Decimal(str(transaction["matecoin_price"])))

    profit["earned_money"], profit["matecoin_account"] \
        = str(profit["earned_money"]), str(profit["matecoin_account"])

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
