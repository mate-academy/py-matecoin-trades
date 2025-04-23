import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    try:
        with open("app/trades.json", "r") as f:
            trades_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File {trades_file} not found.")
        return

    total_earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        bought_str = trade.get("bought")
        sold_str = trade.get("sold")
        price_str = trade.get("matecoin_price")

        if price_str is not None:
            price = Decimal(price_str)
        else:
            continue

        if bought_str is not None:
            bought = Decimal(bought_str)
            cost = bought * price
            matecoin_account += bought
            total_earned_money -= cost
        if sold_str is not None:
            sold = Decimal(sold_str)
            revenue = sold * price
            matecoin_account -= sold
            total_earned_money += revenue

    profit_data = {
        "earned_money": str(total_earned_money.quantize(Decimal("0.0000000"))),
        "matecoin_account": str(matecoin_account.quantize(Decimal("0.00000"))),
    }

    try:
        with open("profit.json", "w") as f:
            json.dump(profit_data, f, indent=2)
        print("Profit information saved to profit.json")
    except IOError as e:
        print(f"Error saving profit information to profit.json: {e}")
