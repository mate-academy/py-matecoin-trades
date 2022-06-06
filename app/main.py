import json
from decimal import Decimal


def calculate_profit(file_name):
    with open(file_name) as f:
        data = json.load(f)
    earned_money = Decimal()
    matecoin_account = Decimal()
    for transaction in data:
        price = Decimal(transaction["matecoin_price"])
        if transaction["bought"]:
            matecoin_account += Decimal(transaction["bought"])
            earned_money -= Decimal(transaction["bought"]) * price
        if transaction["sold"]:
            matecoin_account -= Decimal(transaction["sold"])
            earned_money += Decimal(transaction["sold"]) * price

    result_of_trades = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    print(result_of_trades)

    with open("profit.json", "w") as output_file:
        json.dump(result_of_trades, output_file, indent=2)

