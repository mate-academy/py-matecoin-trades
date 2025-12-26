# write your code here
import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file_in:
        trades = json.load(file_in)

    earned_money = 0
    matecoin_account = 0

    for trade in trades:
        sold = (Decimal(trade["sold"]) if trade["sold"] is not None
                else Decimal("0.0"))
        bought = (Decimal(trade["bought"]) if trade["bought"] is not None
                  else Decimal("0.0"))

        earned_money += Decimal(trade["matecoin_price"]) * (sold - bought)
        matecoin_account += bought - sold

    trades_dict = ({"earned_money": str(earned_money),
                    "matecoin_account": str(matecoin_account)})

    with open("profit.json", "w") as file_out:
        json.dump(trades_dict, file_out, indent=2)
