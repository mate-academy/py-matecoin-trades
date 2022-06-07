import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit = 0
    matecoin_account = 0
    with open(file_name, "r") as file:
        money_data = json.load(file)
    for transaction in money_data:
        spent = 0
        earned = 0
        if transaction["bought"] is not None:
            matecoin_account += Decimal(transaction["bought"])
            spent = Decimal(transaction["bought"]) * Decimal(transaction["matecoin_price"])
        if transaction["sold"] is not None:
            matecoin_account -= Decimal(transaction["sold"])
            earned = Decimal(transaction["sold"]) * Decimal(transaction["matecoin_price"])
        profit += earned - spent
    profit_data = [
        {
            "earned_money": str(profit),
            "matecoin_account": str(matecoin_account)
        }
    ]
    with open("profit.json", "w") as file:
        json.dump(profit_data, file)
