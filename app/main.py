import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    profit = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought, sold, matecoin_price = trade.values()

        sold = Decimal(sold) if sold is not None else Decimal(0)
        bought = Decimal(bought) if bought is not None else Decimal(0)
        matecoin_price = Decimal(matecoin_account)

        profit += (sold - bought) * matecoin_price
        matecoin_account += bought - sold

    with open("profit.json", "w") as file:
        json.dump(
            {
                "earned_money": str(profit),
                "matecoin_account": str(matecoin_account)
            },
            file,
            indent=2
        )
