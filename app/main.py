import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    money_balance = Decimal("0")
    matecoin_balance = Decimal("0")

    for trade in trades:
        if trade:
            bought = trade.get("bought")
            sold = trade.get("sold")
            price = trade.get("matecoin_price")

            if bought is not None:
                money_balance -= Decimal(str(bought)) * Decimal(str(price))
                matecoin_balance += Decimal(str(bought))

            if sold is not None:
                money_balance += Decimal(str(sold)) * Decimal(str(price))
                matecoin_balance -= Decimal(str(sold))

    result = {
        "earned_money": str(money_balance),
        "matecoin_account": str(matecoin_balance),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
