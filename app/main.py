import json
import decimal
import os


def calculate_profit(file_name: str) -> None:
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            data = json.load(f)
    else:
        return None

    spent_money = decimal.Decimal("0")
    earned_money = decimal.Decimal("0")
    matecoin_acc = decimal.Decimal("0")

    for trade in data:
        if trade["bought"] is not None:
            decimal_number = decimal.Decimal(trade["bought"])
            matecoin_acc += decimal_number
            value_bought = (decimal_number
                            * decimal.Decimal(trade["matecoin_price"]))
            spent_money += value_bought

        if trade["sold"] is not None:
            value = (decimal.Decimal(trade["sold"])
                     * decimal.Decimal(trade["matecoin_price"]))
            earned_money += value
            matecoin_acc -= decimal.Decimal(trade["sold"])

    profit = earned_money - spent_money
    result = {"earned_money": str(profit),
              "matecoin_account": str(matecoin_acc)}

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
