import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    data = {
        "earned_money": None,
        "matecoin_account": None
    }
    earned_money = Decimal("0")
    matecoin_count = Decimal("0")

    with open(filename) as file:
        trades = json.load(file)
        for transaction in trades:
            earned_money += account_profit(transaction)
            matecoin_count += account_coins_flow(transaction)

    data["earned_money"] = str(earned_money)
    data["matecoin_account"] = str(matecoin_count)

    with open("profit.json", "w") as file:
        json.dump(data, file, indent=2)


def account_coins_flow(transaction: dict) -> Decimal:
    coins_result = Decimal("0")
    if transaction["bought"]:
        coins_result += Decimal(transaction["bought"])
    if transaction["sold"]:
        coins_result -= Decimal(transaction["sold"])
    return coins_result


def account_profit(transaction: dict) -> Decimal:
    profit_result = Decimal("0")
    if transaction["bought"]:
        profit_result -= Decimal(transaction["bought"]) * \
            Decimal(transaction["matecoin_price"])
    if transaction["sold"]:
        profit_result += Decimal(transaction["sold"]) * \
            Decimal(transaction["matecoin_price"])
    return profit_result
