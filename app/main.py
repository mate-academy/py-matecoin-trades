import json
import os
from decimal import Decimal


trades_path = os.path.join(os.path.dirname(__file__), "trades.json")
DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROFIT = os.path.join(DIR, "profit.json")


def calculate_profit(trades_path: str) -> bool:
    if trades_path == "":
        trades_path = os.path.join(os.path.dirname(__file__), "trades.json")

    with open(trades_path, "r") as file:
        mentors = json.load(file)
        rr1 = Decimal(0)
        rr2 = Decimal(0)

        for rr in mentors:
            if rr.get("bought") is None and rr.get("sold") is not None:
                rr1 = Decimal(rr1) - Decimal(rr.get("sold"))
                rr2 = (
                    Decimal(rr2) + Decimal(rr.get("sold"))
                    * Decimal(rr.get("matecoin_price"))
                )

            elif rr.get("sold") is None and rr.get("bought") is not None:
                rr1 = Decimal(rr1) + Decimal(rr.get("bought"))
                rr2 = (
                    Decimal(rr2) - Decimal(rr.get("bought"))
                    * Decimal(rr.get("matecoin_price"))
                )

            elif rr.get("sold") is not None and rr.get("sold") is not None:
                rr1 = (
                    Decimal(rr1) + Decimal(rr.get("bought"))
                    - Decimal(rr.get("sold"))
                )
                rr2 = (
                    Decimal(rr2)
                    + (Decimal(rr.get("sold"))
                       - Decimal(rr.get("bought")))
                    * Decimal(rr.get("matecoin_price"))
                )
        rr1 = str(rr1)
        rr2 = str(rr2)
        expected1 = {
            "earned_money": rr2,
            "matecoin_account": rr1
        }

        with open(PROFIT, "w") as profit:
            json.dump(expected1, profit, indent=2)
