import decimal
import json


def calculate_profit(trade_inf_file: str) -> None:
    with open(trade_inf_file, "r") as file:
        inf_list = json.load(file)
        money = 0
        matecoin = 0
        for action in inf_list:
            if action["bought"] is not None:
                matecoin += decimal.Decimal(action["bought"])
                money -= (
                    decimal.Decimal(action["bought"])
                    * decimal.Decimal(action["matecoin_price"])
                )
            if action["sold"] is not None:
                matecoin -= decimal.Decimal(action["sold"])
                money += (
                    decimal.Decimal(action["sold"])
                    * decimal.Decimal(action["matecoin_price"])
                )
        profit = {
            "earned_money": str(money),
            "matecoin_account": str(matecoin)
        }
        with open("profit.json", "w") as f:
            json.dump(profit, f, indent=2)
