# write your code here
import json

from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file, "r") as file_in:
        trades = json.load(file_in)
        earn_money_bought = 0
        earn_money_sold = 0
        count_bought = 0
        count_sold = 0
        for trade in trades:
            if trade["bought"] is not None:
                earn_money_bought += (Decimal(trade["bought"])
                                      * Decimal(trade["matecoin_price"]))
                count_bought += Decimal(trade["bought"])

        for trade in trades:
            if trade["sold"] is not None:
                earn_money_sold += (Decimal(trade["sold"])
                                    * Decimal(trade["matecoin_price"]))
                count_sold += Decimal(trade["sold"])

        result = {"earned_money": str(earn_money_sold - earn_money_bought),
                  "matecoin_account": str(count_bought - count_sold)}

    with open("profit.json", "w") as file_out:
        json.dump(result, file_out, indent=2)
