import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file) as f:
        trades = json.load(f)
        total_purchases = Decimal("0")
        total_sales = Decimal("0")
        purchase_amount = Decimal("0")
        sales_amount = Decimal("0")
        for trade in trades:
            if not trade.get("bought") is None:
                purchase_amount += (Decimal(trade["matecoin_price"])
                                    * Decimal(trade["bought"]))
                total_purchases += Decimal(trade["bought"])
            if not trade.get("sold") is None:
                sales_amount += (Decimal(trade["matecoin_price"])
                                 * Decimal(trade["sold"]))
                total_sales += Decimal(trade["sold"])

        profit = {
            "earned_money": str(sales_amount - purchase_amount),
            "matecoin_account": str(total_purchases - total_sales)
        }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
