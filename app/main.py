import json
from decimal import Decimal


def calculate_profit(trades_file: str,
                     output_file: str = "../profit.json",
                     ) -> None:
    with (open(trades_file) as copy,
          open(output_file, "w") as paste):
        trades = json.load(copy)
        earned_money = Decimal(0)
        matecoin_account = Decimal(0)

        for trade in trades:
            matecoin_price = Decimal(trade["matecoin_price"])
            if trade["bought"]:
                bought_volume = Decimal(trade["bought"])
                matecoin_account += bought_volume
                earned_money -= bought_volume * matecoin_price
            if trade["sold"]:
                sold_volume = Decimal(trade["sold"])
                matecoin_account -= sold_volume
                earned_money += sold_volume * matecoin_price
        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        json.dump(result, paste, indent=2)
