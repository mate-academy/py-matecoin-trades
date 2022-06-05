from decimal import Decimal as D
import json


def calculate_profit():
    with open("trades.json") as fin, open("profit.json", "a") as fout:
        content = json.load(fin)
        income = D()
        amount = D()
        for row in content:
            if row["bought"] is not None:
                income -= D(row["bought"]) * D(row["matecoin_price"])
                amount += D(row["bought"])
            if row["sold"] is not None:
                income += D(row["sold"]) * D(row["matecoin_price"])
                amount -= D(row["sold"])
        outcome = {
            "earned_money": str(income),
            "matecoin_account": str(amount)
        }
        json.dump(outcome, fout, indent=2)
