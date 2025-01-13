import json
from decimal import Decimal


def calculate_profit(file_name: str = "trades.json") -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)

        if not isinstance(trades, list):
            raise ValueError

        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for trade in trades:
            if trade["bought"] is not None:
                bought_volume = Decimal(trade["bought"])
                matecoin_price = Decimal(trade["matecoin_price"])
                matecoin_account += bought_volume
                earned_money -= bought_volume * matecoin_price

            if trade["sold"] is not None:
                sold_volume = Decimal(trade["sold"])
                matecoin_price = Decimal(trade["matecoin_price"])
                matecoin_account -= sold_volume
                earned_money += sold_volume * matecoin_price

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }

        with open("profit.json", "w") as pro:
            json.dump(result, pro, ensure_ascii=False, indent=2)
