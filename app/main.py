import os
import json
from decimal import Decimal


os.chdir(os.path.dirname(os.path.abspath(__file__)))


def calculate_profit(file_name: str) -> None:

    with open(os.path.join(os.getcwd(), file_name), "r") as file:

        trades = json.load(file)

    total_spent = Decimal(0)
    total_earned = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = Decimal(trade["matecoin_price"])

        if bought:
            total_spent += Decimal(bought) * price
            matecoin_account += Decimal(bought)
        if sold:
            total_earned += Decimal(sold) * price
            matecoin_account -= Decimal(sold)

    profit = total_earned - total_spent

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_account)
    }

    output_path = os.path.abspath(os.path.join(
        os.getcwd(),
        os.pardir,
        "profit.json"
    ))

    with open(output_path, "w") as outfile:
        json.dump(result, outfile, indent=2)
