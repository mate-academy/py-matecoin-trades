import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as trades:
        coins = json.load(trades)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for coin in coins:
        bought, sold, matecoin_price = coin.values()
        if bought:
            matecoin_account += Decimal(bought)
            earned_money -= Decimal(bought) * Decimal(matecoin_price)
        if sold:
            matecoin_account -= Decimal(sold)
            earned_money += Decimal(sold) * Decimal(matecoin_price)

    profit_result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit:
        json.dump(profit_result, profit, indent=2)
