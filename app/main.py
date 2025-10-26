from decimal import Decimal
import json


def calculate_profit(fail_name: str) -> None:

    with open(fail_name, "r") as json_data:
        trades_data = json.load(json_data)
        result_dict = {}
        matecoin_account = Decimal("0")
        earned_money = Decimal("0")
        for trade in trades_data:
            if trade["bought"] is not None:

                matecoin_account += Decimal(trade["bought"])
                earned_money -= Decimal(trade["bought"]
                                        ) * Decimal(trade["matecoin_price"])
            if trade["sold"] is not None:
                matecoin_account -= Decimal(trade["sold"])
                earned_money += Decimal(trade["sold"]
                                        ) * Decimal(trade["matecoin_price"])

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
