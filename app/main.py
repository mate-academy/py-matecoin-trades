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

        matecoin_account_str = str(matecoin_account)
        earned_money_str = str(earned_money)
        result_dict["earned_money"] = earned_money_str
        result_dict["matecoin_account"] = matecoin_account_str

    with open("profit.json", "w") as f:
        json.dump(result_dict, f, indent=2)


calculate_profit("trades.json")
