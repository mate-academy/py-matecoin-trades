import json
from decimal import Decimal


def calculate_profit(json_file: json) -> None:
    report = {
        "earned_money": Decimal("0.0"),
        "matecoin_account": Decimal("0.0")
    }
    with open(json_file, "r") as out:
        data = json.load(out)
        for trade in data:
            bought = Decimal(trade.get("bought") or "0")
            sold = Decimal(trade.get("sold") or "0")
            price = Decimal(trade.get("matecoin_price"))

            report["earned_money"] += sold * price - bought * price
            report["matecoin_account"] += bought - sold

    report["earned_money"] = str(report["earned_money"])
    report["matecoin_account"] = str(report["matecoin_account"])
    with open("profit.json", "w") as into:
        json.dump(report, into, indent=2)
