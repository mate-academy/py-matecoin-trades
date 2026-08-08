import json
from decimal import Decimal


def calculate_profit(file_json: json) -> None:
    with open(file_json, "r") as file:
        trades = json.load(file)

    bought = 0
    sold = 0
    matecoin_account = 0
    for trade in trades:
        if trade["bought"]:
            bought += (Decimal(str(trade["bought"]))
                       * Decimal(str(trade["matecoin_price"])))
            matecoin_account += Decimal(str(trade["bought"]))
        if trade["sold"]:
            sold += (Decimal(str(trade["sold"]))
                     * Decimal(str(trade["matecoin_price"])))
            matecoin_account -= Decimal(str(trade["sold"]))

    profit = {
        "earned_money": str(sold - bought),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
