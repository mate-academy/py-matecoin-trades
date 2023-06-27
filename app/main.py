import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    sold_price_total = 0
    bought_price_total = 0
    account = 0

    with open(file_name) as file_stats:
        stats = json.load(file_stats)

    for trade in stats:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = trade.get("matecoin_price")

        if bought:
            bought_price_total += (Decimal(bought) * Decimal(price))
            account += Decimal(bought)

        if sold:
            sold_price_total += Decimal(sold) * Decimal(price)
            account -= Decimal(sold)

    profit = {
        "earned_money": str(sold_price_total - bought_price_total),
        "matecoin_account": str(account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
