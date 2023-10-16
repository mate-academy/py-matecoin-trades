from _decimal import Decimal
from typing import Any
import json


def calculate_profit(trades: Any) -> Any:
    with open(trades, "r") as read_file:
        data = json.load(read_file)
        bought = 0
        sold = 0
        mpb = 0
        mps = 0
        for detail in data:
            if detail.get("bought") is not None:
                bought += Decimal(detail.get("bought"))
                mpb += (Decimal(detail.get("bought"))
                        * Decimal(detail.get("matecoin_price")))
            if detail.get("sold") is not None:
                sold += Decimal(detail.get("sold"))
                mps += (Decimal(detail.get("sold"))
                        * Decimal(detail.get("matecoin_price")))
        dict_of_profit = {"earned_money": str(mps - mpb),
                          "matecoin_account": str(bought - sold)}
        with open("profit.json", "w") as write_file:
            json.dump(dict_of_profit, write_file, indent=2)
