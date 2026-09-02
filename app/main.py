import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(trades_path: str) -> None:
    with open(trades_path) as f:
        trade_data_py = json.load(f)
    balance = Decimal("0")
    matecoins = Decimal("0")
    resulted_dict = {}
    for elem in trade_data_py:
        if elem["bought"] is not None:
            balance -= (Decimal(elem["matecoin_price"])
                        * Decimal(elem["bought"]))
            matecoins += Decimal(elem["bought"])
        if elem["sold"] is not None:
            balance += (Decimal(elem["matecoin_price"])
                        * Decimal(elem["sold"]))
            matecoins -= Decimal(elem["sold"])
    resulted_dict.update(
        {"earned_money": str(balance),
         "matecoin_account": str(matecoins)
         }
    )

    profit_path = Path(trades_path).resolve().parent.parent / "profit.json"
    with open(profit_path, "w") as f:
        json.dump(resulted_dict, f, indent=2)
