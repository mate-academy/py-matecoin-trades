import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades = json.load(f)

    matecoins_count = Decimal("0")
    matecoins_money = Decimal("0")

    for trade in trades:
        try:
            if trade.get("bought") is not None:
                matecoins_count += Decimal(trade["bought"])
                matecoins_money -= (Decimal(trade["bought"])
                                    * Decimal(trade["matecoin_price"]))
            if trade.get("sold") is not None:
                matecoins_count -= Decimal(trade["sold"])
                matecoins_money += (Decimal(trade["sold"])
                                    * Decimal(trade["matecoin_price"]))
        except (TypeError, ValueError) as e:
            print(f"Wrong type {trade} - Error {e}")

    wallet = {
        "earned_money": str(matecoins_money),
        "matecoin_account": str(matecoins_count)
    }

    with open("profit.json", "w") as output_file:
        json.dump(wallet, output_file, indent=2)
