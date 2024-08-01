import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as file:
        trades_information = json.load(file)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for session in trades_information:
        if session["bought"] is not None:
            earned_money -= (Decimal(session["bought"])
                             * Decimal(session["matecoin_price"]))
            matecoin_account += Decimal(session["bought"])

        if session["sold"] is not None:
            earned_money += (Decimal(session["sold"])
                             * Decimal(session["matecoin_price"]))
            matecoin_account -= Decimal(session["sold"])

    profit_info = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit:
        json.dump(profit_info, profit, indent=2)
