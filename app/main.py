import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with (open(filename, "r") as input_file,
          open("profit.json", "w") as output_file):
        trades_data = json.load(input_file)
        profit_dict = {"earned_money": 0, "matecoin_account": 0}
        for trades in trades_data:
            if trades["bought"]:
                profit_dict["earned_money"] -= \
                    (Decimal(trades["bought"]) *Decimal\
                        (trades["matecoin_price"]))
                profit_dict["matecoin_account"] += \
                    Decimal(trades["bought"])
            if trades["sold"]:
                profit_dict["earned_money"] += \
                    (Decimal(trades["sold"]) * Decimal\
                        (trades["matecoin_price"]))
                profit_dict["matecoin_account"] -= Decimal(trades["sold"])
        for key, value in profit_dict.items():
            profit_dict[key] = str(value)

        json.dump(profit_dict, output_file, indent=2)
