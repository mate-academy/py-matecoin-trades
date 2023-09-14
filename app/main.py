import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    with open(name, "r") as my_json_file:
        trades = json.load(my_json_file)

    erned_money = 0
    matecoin = 0
    for trade in trades:
        if trade["bought"] is not None:
            erned_money -= (
                Decimal(str(trade["bought"]))
                * Decimal(str(trade["matecoin_price"]))
            )
            matecoin += Decimal(str(trade["bought"]))
        if trade["sold"] is not None:
            erned_money += (
                Decimal(str(trade["sold"]))
                * Decimal(str(trade["matecoin_price"]))
            )
            matecoin -= Decimal(str(trade["sold"]))

    fin = {
        "earned_money": str(erned_money),
        "matecoin_account": str(matecoin)
    }

    with open("profit.json", "w") as json_file:
        json.dump(fin, json_file, indent=2)
