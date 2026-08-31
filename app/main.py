import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as json_trades:
        data = json.load(json_trades)
    earned_money = Decimal("0")
    currency = Decimal("0")
    for transaction in data:
        if transaction["bought"]:
            bought_curr = Decimal(transaction["bought"])
            currency += bought_curr
            earned_money -= (Decimal(transaction["matecoin_price"])
                             * bought_curr)
        if transaction["sold"]:
            sold_curr = Decimal(transaction["sold"])
            currency -= sold_curr
            earned_money += Decimal(transaction["matecoin_price"]) * sold_curr
    result_profits = {
        "earned_money": str(earned_money),
        "matecoin_account": str(currency)
    }
    with open("profit.json", "w") as profits_json:
        json.dump(result_profits, profits_json, indent=2)
