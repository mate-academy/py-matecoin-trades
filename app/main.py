import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades_json = json.load(file)

    money = Decimal(0)
    coins = Decimal(0)

    for trade in trades_json:
        if trade["bought"] and trade["sold"]:
            money += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            coins -= Decimal(trade["sold"])
            money -= Decimal(
                trade["bought"]) * Decimal(trade["matecoin_price"])
            coins += Decimal(trade["bought"])

        if trade["bought"] and not trade["sold"]:
            money -= Decimal(
                trade["bought"]) * Decimal(trade["matecoin_price"])
            coins += Decimal(trade["bought"])

        if trade["sold"] and not trade["bought"]:
            money += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            coins -= Decimal(trade["sold"])

    result_dict = {"earned_money": str(money), "matecoin_account": str(coins)}

    with open("profit.json", "w") as file:
        json.dump(result_dict, file, indent=2)


if __name__ == "__main__":
    calculate_profit("app/trades.json")
