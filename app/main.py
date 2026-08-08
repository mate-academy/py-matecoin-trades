import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    money_profit = Decimal("0")
    current_coin_account = Decimal("0")

    with open(file_name, "r") as trades:
        trades_data = json.load(trades)

    for data in trades_data:
        matecoin_price_data = Decimal(data["matecoin_price"])
        if data["bought"]:
            money_profit -= Decimal(data["bought"]) * matecoin_price_data
            current_coin_account += Decimal(data["bought"])
        if data["sold"]:
            money_profit += Decimal(data["sold"]) * matecoin_price_data
            current_coin_account -= Decimal(data["sold"])

    profit = {
        "earned_money": str(money_profit),
        "matecoin_account": str(current_coin_account)
    }
    with open("profit.json", "w") as result:
        json.dump(profit, result, indent=2)
