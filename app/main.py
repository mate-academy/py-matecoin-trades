import decimal
import json


def calculate_profit(trades_path: str) -> None:
    matecoin_account = 0
    earned_money = 0

    with open(trades_path) as file:
        op_data = json.load(file)
    for op in op_data:
        if op["bought"] is not None and op["sold"] is None:
            money_for_each_op = (decimal.Decimal(op["matecoin_price"])
                                 * decimal.Decimal(op["bought"]))
            matecoin_account += decimal.Decimal(op["bought"])
            earned_money -= money_for_each_op
        elif op["bought"] is not None and op["sold"] is not None:
            money_for_each_op = (decimal.Decimal(op["matecoin_price"])
                                 * decimal.Decimal(op["bought"]))
            money_for_each_sold = (decimal.Decimal(op["matecoin_price"])
                                   * decimal.Decimal(op["sold"]))
            matecoin_account += decimal.Decimal(op["bought"])
            matecoin_account -= decimal.Decimal(op["sold"])
            earned_money += money_for_each_sold
            earned_money -= money_for_each_op
        elif op["bought"] is None and op["sold"] is not None:
            money_for_each_op = (decimal.Decimal(op["matecoin_price"])
                                 * decimal.Decimal(op["sold"]))
            matecoin_account -= decimal.Decimal(op["sold"])
            earned_money += money_for_each_op
    with open("profit.json", "w") as new_file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            }, new_file, indent=2)
