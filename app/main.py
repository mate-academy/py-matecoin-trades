from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    bought_total = 0
    sold_total = 0
    account = 0

    with open(file_name) as f:
        stats = json.load(f)

    for trade in stats:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = trade.get("matecoin_price")

        if bought:
            bought_total += (Decimal(bought) * Decimal(price))
            account += Decimal(bought)

        if sold:
            sold_total += (Decimal(sold) * Decimal(price))
            account -= Decimal(sold)

    profit = {
        "earned_money": str(sold_total - bought_total),
        "matecoin_account": str(account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
