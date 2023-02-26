import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as file:
        trades_list = json.load(file)
    matecoin_account = 0
    bought = 0
    sold = 0
    for deal in trades_list:
        if deal["bought"]:
            matecoin_account += Decimal(deal["bought"])
            bought += Decimal(deal["bought"]) * Decimal(deal["matecoin_price"])
        if deal["sold"]:
            matecoin_account -= Decimal(deal["sold"])
            sold += Decimal(deal["sold"]) * Decimal(deal["matecoin_price"])
    profit = {
        "earned_money": str(sold - bought),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
