from decimal import Decimal
import json

with open("trades.json", "r") as file_trades:
    open_file = json.load(file_trades)


def calculate_profit(date_trades: list) -> dict:
    total_coins = Decimal("0")
    purchase_costs = Decimal("0")
    revenue_from_sales = Decimal("0")
    result = {}

    for item in date_trades:
        if item["bought"] is not None:
            total_coins += Decimal(item["bought"])
            purchase_costs += Decimal(item["bought"]) * Decimal(item["matecoin_price"])

        if item["sold"] is not None:
            revenue_from_sales += Decimal(item["sold"]) * Decimal(item["matecoin_price"])
            revenue_from_sales += Decimal(item["sold"])
            total_coins -= Decimal(item["sold"])
            profit = Decimal(revenue_from_sales) - Decimal(purchase_costs)

    result["earned_money"] = str(profit)
    result["matecoin_account"] = str(total_coins)
    return result


with open("profit.json", "a") as file_profit:
    json.dump(calculate_profit(open_file), file_profit, indent=2)
