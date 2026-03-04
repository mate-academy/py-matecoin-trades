import json
from decimal import Decimal


def calculate_profit(json_file: str) -> None:
    with open(json_file, "r") as trades:
        my_wallet = json.load(trades)

    matecoin_result = Decimal("0")
    bght = Decimal("0")
    sold = Decimal("0")
    calculate = {
        "earned_money": 0,
        "matecoin_account": 0
    }
    for coin in my_wallet:
        if coin["bought"] is not None:
            matecoin_result += Decimal(coin["bought"])
            bght += (Decimal(coin["bought"]) * Decimal(coin["matecoin_price"]))

        if coin["sold"] is not None:
            matecoin_result -= Decimal(coin["sold"])
            sold += (Decimal(coin["sold"]) * Decimal(coin["matecoin_price"]))

    calculate["earned_money"] = str(sold - bght)
    calculate["matecoin_account"] = str(matecoin_result)

    with open("profit.json", "w") as profit:
        json.dump(calculate, profit, indent=2)
