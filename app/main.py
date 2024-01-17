from decimal import Decimal
import json


def calculate_profit(file_json: str) -> None:
    with open(str(file_json), "r") as file:
        trades_data = json.load(file)

    earned_money = 0
    matecoin_account = 0

    for trade in trades_data:
        if trade["bought"] is not None:
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
        if trade["sold"] is not None:
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))

    for trade in trades_data:
        bought_amount = Decimal(trade.get("bought", 0) or 0)
        sold_amount = Decimal(trade.get("sold", 0) or 0)

        matecoin_account += bought_amount - sold_amount

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
