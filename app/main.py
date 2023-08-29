import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        trades = json.load(file)

    matecoins_account = Decimal("0.0")
    earned_money = Decimal("0.0")
    for trade in trades:
        bought, sold, matecoin_price = trade.values()
        if bought is not None:
            matecoins_account += Decimal(bought)
            earned_money -= Decimal(Decimal(bought) * Decimal(matecoin_price))
        if sold is not None:
            matecoins_account -= Decimal(sold)
            earned_money += Decimal(Decimal(sold) * Decimal(matecoin_price))

    profit_of_trades = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoins_account)
    }
    with open("profit.json", "w") as file:
        json.dump(profit_of_trades, file, indent=2)
