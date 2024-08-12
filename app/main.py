import json
from decimal import Decimal
import os


def calculate_profit(trades: str) -> None:
    with open(trades) as file_trades:
        trades_list = json.load(file_trades)
    sum_buy = Decimal("0")
    sum_sold = Decimal("0")
    account = Decimal("0")
    for trad in trades_list:
        if trad.get("bought") is not None:
            sum_buy += (
                Decimal(trad["bought"]) * Decimal(trad["matecoin_price"])
            )
            account += Decimal(trad["bought"])
        if trad.get("sold") is not None:
            sum_sold += (
                Decimal(trad["sold"]) * Decimal(trad["matecoin_price"])
            )
            account -= Decimal(trad["sold"])

    earned = sum_sold - sum_buy

    result = {
        "earned_money": str(earned),
        "matecoin_account": str(account)
    }
    output_path = os.path.join(
        "/Users/lera/PycharmProjects/py-matecoin-trades/",
        "profit.json"
    )
    with open(output_path, "w") as final_file:
        json.dump(result, final_file, indent=2)
