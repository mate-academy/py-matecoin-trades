import json
from decimal import Decimal


def calculate_profit(trades_file_name: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(trades_file_name) as trades_file:
        trades_dict = json.load(trades_file)
        for trade in trades_dict:
            if trade["bought"] is not None:
                earned_money -= (Decimal(str(trade["bought"]))
                                 * Decimal(trade["matecoin_price"]))
                matecoin_account += Decimal(trade["bought"])
            if trade["sold"] is not None:
                earned_money += (Decimal(str(trade["sold"]))
                                 * Decimal(trade["matecoin_price"]))
                matecoin_account -= Decimal(trade["sold"])

    with open("profit.json", "w") as res_file:
        trading_result = dict(
            earned_money=str(earned_money),
            matecoin_account=str(matecoin_account),
        )
        json.dump(trading_result, res_file, indent=2)
