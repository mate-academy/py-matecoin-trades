import json
from decimal import Decimal


def calculate_profit(trades: json) -> None:

    with open(trades) as file:
        trades_data = json.load(file)

    profit = Decimal(0.0)
    metacoins = Decimal(0)

    for trade in trades_data:
        bought, sold, matecoin_price = trade.values()
        print(bought, sold, matecoin_price)

        if bought:
            profit -= Decimal(bought) * Decimal(matecoin_price)
            metacoins += Decimal(bought)
        if sold:
            profit += Decimal(sold) * Decimal(matecoin_price)
            metacoins -= Decimal(sold)

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(metacoins)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
