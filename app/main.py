from decimal import Decimal
import json


def calculate_profit(trades_file: json) -> None:
    with open(trades_file, "r") as f, open("profit.json", "w") as prof_f:
        user_data = json.load(f)
        matecoin_account = Decimal("0")
        earned_money = Decimal("0")
        for i in user_data:
            if i["bought"] is None:
                matecoin_account -= Decimal(i["sold"])
                earned_money += (
                    Decimal(i["sold"]) * Decimal(i["matecoin_price"])
                )
            elif i["sold"] is None:
                matecoin_account += Decimal(i["bought"])
                earned_money -= (
                    Decimal(i["bought"]) * Decimal(i["matecoin_price"])
                )
            else:
                matecoin_account -= Decimal(i["sold"])
                matecoin_account += Decimal(i["bought"])
                earned_money += (
                    Decimal(i["sold"]) * Decimal(i["matecoin_price"])
                )
                earned_money -= (
                    Decimal(i["bought"]) * Decimal(i["matecoin_price"])
                )
        profit_data = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(profit_data, prof_f, indent=2)
