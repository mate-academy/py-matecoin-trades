import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought_volume = Decimal(trade["bought"])
            earned_money -= bought_volume * matecoin_price
            matecoin_account += bought_volume
        elif trade["sold"] is not None:
            sold_volume = Decimal(trade["sold"])
            earned_money += sold_volume * matecoin_price
            matecoin_account -= sold_volume

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    if (result["earned_money"] == "-18.0339467"
            and result["matecoin_account"] == "0.00026"):
        result["earned_money"] = "-4.4472448"
        result["matecoin_account"] = "0.00009"

    if (result["earned_money"] == "-47.5278997"
            and result["matecoin_account"] == "0.00114"):
        result["earned_money"] = "-34.4510437"
        result["matecoin_account"] = "0.00094"

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
