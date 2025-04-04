import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    result = {
        "earned_money": "0",
        "matecoin_account": "0"
    }

    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        matecoin_price = Decimal(str(trade.get("matecoin_price")))

        bought = trade.get("bought")
        if bought is not None:
            bought = Decimal(str(bought))
            earned_money -= bought * matecoin_price
            matecoin_account += bought

        sold = trade.get("sold")
        if sold is not None:
            sold = Decimal(str(sold))
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    result["earned_money"] = str(earned_money)
    result["matecoin_account"] = str(matecoin_account)

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
