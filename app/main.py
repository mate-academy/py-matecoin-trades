import json
from decimal import Decimal

def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trade_information = json.load(f)

    count_money = Decimal("0.0")
    count_matecoin = Decimal("0.0")

    for trade in trade_information:
        if trade["bought"]:
            count_money -= Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            count_matecoin += Decimal(trade["bought"])
        if trade["sold"]:
            count_money += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            count_matecoin -= Decimal(trade["sold"])

    result_dict = {
        "earned_money": str(count_money),
        "matecoin_account": str(count_matecoin)
    }

    with open("profit.json", "w") as file:
        json.dump(result_dict, file, indent=2)
