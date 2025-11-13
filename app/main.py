import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file, "r") as json_file:
        data_trades = json.load(json_file)

    balance_in_usd = Decimal("0")
    balance_in_matecoin = Decimal("0")
    for trade in data_trades:
        if trade.get("bought") is not None:
            balance_in_usd -= (
                Decimal(trade.get("bought"))
                * Decimal(trade.get("matecoin_price"))
            )
            balance_in_matecoin += Decimal(trade.get("bought"))
        if trade.get("sold") is not None:
            balance_in_usd += (
                Decimal(trade.get("sold"))
                * Decimal(trade.get("matecoin_price"))
            )
            balance_in_matecoin -= Decimal(trade.get("sold"))

    total_profit = {"earned_money": str(balance_in_usd),
                    "matecoin_account": str(balance_in_matecoin)
                    }

    with open("profit.json", "w") as json_file:
        json.dump(total_profit, json_file)
