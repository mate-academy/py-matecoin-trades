import json
from decimal import Decimal


def calculate_profit(file_trades: str) -> None:
    earned_money = 0
    matecoin_account = 0
    with (open(file_trades) as trades_file):
        trades_data = json.load(trades_file)
        for trade in trades_data:
            if trade["bought"] is not None and trade["sold"] is None:
                matecoin_account += Decimal(trade["bought"])
                earned_money -= (Decimal(trade["bought"])
                                 * Decimal(trade["matecoin_price"]))
            elif trade["sold"] is not None and trade["bought"] is None:
                matecoin_account -= Decimal(trade["sold"])
                earned_money += (Decimal(trade["sold"])
                                 * Decimal(trade["matecoin_price"]))
            else:
                matecoin_account += Decimal(trade["bought"])
                matecoin_account -= Decimal(trade["sold"])
                earned_money -= (Decimal(trade["bought"])
                                 * Decimal(trade["matecoin_price"]))
                earned_money += (Decimal(trade["sold"])
                                 * Decimal(trade["matecoin_price"]))

    with open("profit.json", "w") as profit_file:
        json.dump({"earned_money": str(Decimal(earned_money)),
                   "matecoin_account": str(Decimal(matecoin_account))},
                  profit_file, indent=2)
