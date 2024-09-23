import json
from decimal import Decimal


def calculate_profit(
    trades_file: str,
    profit_file: str = "profit.json",
) -> None:
    with open(trades_file, "r") as file:
        trades_data = json.load(file)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")
    for trade in trades_data:
        bought, sold, price = (
            trade.get("bought"),
            trade.get("sold"),
            trade.get("matecoin_price")
        )
        if bought:
            earned_money -= Decimal(bought) * Decimal(price)
            matecoin_account += Decimal(bought)
        if sold:
            earned_money += Decimal(sold) * Decimal(price)
            matecoin_account -= Decimal(sold)

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open(profit_file, "w") as file:
        json.dump(result, file, indent=2)
