import json
from decimal import Decimal
import os


def calculate_profit(name_trades: str) -> None:
    with open(name_trades) as trades_f:
        list_trades = json.load(trades_f)

    sold = Decimal("0")
    trades_dict = {"earned_money": Decimal("0"),
                   "matecoin_account": Decimal("0")}

    for trades in list_trades:

        if trades["bought"]:
            trades_dict["earned_money"] \
                += Decimal(trades["matecoin_price"]) * -Decimal(
                trades["bought"])

            trades_dict["matecoin_account"] += Decimal(trades["bought"])

        if trades["sold"]:
            trades_dict["earned_money"] \
                += Decimal(trades["matecoin_price"]) * Decimal(trades["sold"])

            sold += Decimal(trades["sold"])

    trades_dict["matecoin_account"] = trades_dict["matecoin_account"] - sold

    trades_dict["earned_money"] = str(trades_dict["earned_money"])

    trades_dict["matecoin_account"] = str(trades_dict["matecoin_account"])

    opo = os.path.join("/Users/bythewaters/py-matecoin-trades/profit.json")
    with open(opo, "w") as profit:

        json.dump(trades_dict, profit, indent=2)
