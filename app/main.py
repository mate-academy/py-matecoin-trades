import json
import decimal


def calculate_profit(json_file: str) -> None:
    with (open(json_file, "r") as f):
        profits = json.load(f)
        matecoin_account = decimal.Decimal("0.00000")
        earned_money = decimal.Decimal("0.0000000")
        for action in profits:
            if action["sold"] is None:
                matecoin_account += decimal.Decimal(action["bought"])
                money_by = (decimal.Decimal(action["bought"])
                            * decimal.Decimal(action["matecoin_price"]))
                earned_money -= money_by
            if action["bought"] is None:
                matecoin_account -= decimal.Decimal(action["sold"])
                money_sol = (decimal.Decimal(action["sold"])
                             * decimal.Decimal(action["matecoin_price"]))
                earned_money += money_sol
            if action["sold"] is not None and action["bought"] is not None:
                matecoin_account += decimal.Decimal(action["bought"])
                matecoin_account -= decimal.Decimal(action["sold"])
                money_by = (decimal.Decimal(action["sold"])
                            * decimal.Decimal(action["matecoin_price"]))
                money_sol = (decimal.Decimal(action["bought"])
                             * decimal.Decimal(action["matecoin_price"]))
                earned_money += (money_by - money_sol)

    result_dict = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}
    with (open("profit.json", "w")) as file:
        json.dump(result_dict, file, indent=2)
