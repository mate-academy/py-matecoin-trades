import json
from decimal import Decimal


def calculate_profit(file_name):
    with open(file_name) as file:
        trades_data = json.load(file)

    earned_money = Decimal()
    matecoin_account = Decimal()

    for operacion in trades_data:
        price = Decimal(operacion["matecoin_price"])
        if operacion["bought"]:
            matecoin_account += Decimal(operacion["bought"])
            earned_money -= Decimal(operacion["bought"]) * price
        else:
            matecoin_account -= Decimal(operacion["sold"])
            earned_money += Decimal(operacion["sold"]) * price

    result_of_trades = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as output_file:
        json.dump(result_of_trades, output_file, indent=2)
