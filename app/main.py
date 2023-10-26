import json
from _pydecimal import Decimal


def calculate_profit(trades_json: str) -> None:
    with open(trades_json) as file:
        trade_list = json.load(file)
        # print(trade_list)
        earned_money = 0
        matecoin_account = 0
        for trade in trade_list:
            trade["sold"] = (0 if trade["sold"] is None
                             else Decimal(trade["sold"]))

            trade["bought"] = (0 if trade["bought"] is None
                               else Decimal(trade["bought"]))

            earned_money += ((trade["sold"] - trade["bought"])
                             * Decimal(trade["matecoin_price"]))

            matecoin_account += (trade["bought"] - trade["sold"])

        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        with open("profit.json", "w") as f:
            json.dump(profit, f, indent=2)
