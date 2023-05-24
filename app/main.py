import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as sessions_file:
        sessions = json.load(sessions_file)

        earned_money = 0
        matecoin_account = 0

        for session in sessions:
            if session["bought"]:
                earned_money -= (Decimal(session["bought"])
                                 * Decimal(session["matecoin_price"]))
                matecoin_account += Decimal(session["bought"])
            if session["sold"]:
                earned_money += (Decimal(session["sold"])
                                 * Decimal(session["matecoin_price"]))
                matecoin_account -= Decimal(session["sold"])

        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as profit_file:
            json.dump(profit, profit_file, indent=2)
