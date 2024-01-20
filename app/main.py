import json

from decimal import Decimal


def calculate_profit(filename: str) -> None:
    result = {"earned_money": "", "matecoin_account": ""}
    with (open(filename, "r") as f_out, open("profit.json", "w") as f_in):
        trade_data = json.load(f_out)
        balance = 0
        coins = 0
        for data in trade_data:
            if data["bought"] is not None:
                balance -= Decimal(data["bought"]) \
                    * Decimal(data["matecoin_price"])
                coins += Decimal(data["bought"])
            if data["sold"] is not None:
                balance += Decimal(data["sold"]) \
                    * Decimal(data["matecoin_price"])
                coins -= Decimal(data["sold"])

        result["earned_money"] = str(balance)
        result["matecoin_account"] = str(coins)
        json.dump(result, f_in, indent=2)
