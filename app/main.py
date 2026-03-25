import json
from decimal import Decimal
from typing import Any


def calculate_profit(trades: Any) -> Any:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(trades) as file:
        data = json.load(file)
        for item in data:

            bought = Decimal(item.get("bought") or "0")
            sold = Decimal(item.get("sold") or "0")
            price = Decimal(item.get("matecoin_price") or "0")
            matecoin_account += (bought - sold)
            earned_money += (sold - bought) * price

    profit_dict = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as file_json:
        json.dump(profit_dict, file_json)
