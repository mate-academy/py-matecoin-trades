from decimal import Decimal
import json


def calculate_profit(trades_file: json) -> None:
    with open(trades_file) as trades_info:
        trades = json.load(trades_info)

    profit = 0
    account = 0

    for trade in trades:
        sold = trade.get("sold")
        bought = trade.get("bought")
        price = trade.get("matecoin_price")

        if bought:
            profit -= (Decimal(bought) * Decimal(price))
            account += Decimal(bought)

        if sold:
            profit += (Decimal(sold) * Decimal(price))
            account -= Decimal(sold)

    with open("./profit.json", "w") as profit_info:
        json.dump(
            {
                "earned_money": str(profit),
                "matecoin_account": str(account)
            },
            profit_info,
            indent=2
        )
