from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data = json.load(file)
    money = Decimal("0")
    mate_coins = Decimal("0")

    for trade in data:
        if trade["bought"] is not None:
            money -= Decimal(
                trade["bought"]) * Decimal(
                    trade["matecoin_price"])
            mate_coins += Decimal(trade["bought"])

        if trade["sold"] is not None:
            money += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            mate_coins -= Decimal(trade["sold"])

    result = {"earned_money": str(money), "matecoin_account": str(mate_coins)}

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
