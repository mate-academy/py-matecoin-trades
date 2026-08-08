import json
from decimal import Decimal


def calculate_profit(way_file: str) -> None:
    with open(way_file, "r") as file:
        trade_data = json.load(file)

    balance_matecoin = 0
    spent = 0
    earned = 0

    for trade in trade_data:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = Decimal(trade["matecoin_price"])
        if bought is not None:
            balance_matecoin += Decimal(bought)
            spent += Decimal(bought) * price
        if sold is not None:
            balance_matecoin -= Decimal(sold)
            earned += Decimal(sold) * price

    profit = earned - spent

    results = {
        "earned_money": str(profit),
        "matecoin_account": str(balance_matecoin)
    }

    with open("profit.json", "w") as output_file:
        json.dump(results, output_file, indent=2, separators=(",", ": "))
