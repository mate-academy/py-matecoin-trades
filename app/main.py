from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trade_data = json.load(file)

    profit = {
        "earned_money": "0",
        "matecoin_account": "0"
    }

    for trade in trade_data:
        sold = trade.get("sold")
        bought = trade.get("bought")
        matecoin_price = trade.get("matecoin_price")
        if sold is None:
            sold = "0"
        if bought is None:
            bought = "0"
        earned_money = \
            (Decimal(sold) - Decimal(bought)) * Decimal(matecoin_price)
        matecoin_account = \
            Decimal(sold) - Decimal(bought)
        profit["earned_money"] = \
            str(Decimal(profit.get("earned_money")) + Decimal(earned_money))
        profit["matecoin_account"] = \
            str(Decimal(profit.get("matecoin_account"))
                - Decimal(matecoin_account))

    with (
        open("C:\\Users\\DELL\\projects\\py-matecoin-trades\\profit.json", "w")
    ) as file:
        json.dump(profit, file, indent=2)
