import json
import decimal


def calculate_profit(name_file: str, null: None = None) -> None:
    earned_money = 0
    matecoin_account = 0
    with open(name_file) as file:
        profits = json.load(file)
        for profit in profits:
            if profit["bought"] is null:
                matecoin_account -= decimal.Decimal(profit["sold"])
                earned_money += (decimal.Decimal(profit["sold"])
                                 * decimal.Decimal(profit["matecoin_price"]))
            elif profit["sold"] is null:
                matecoin_account += decimal.Decimal(profit["bought"])
                earned_money -= (decimal.Decimal(profit["bought"])
                                 * decimal.Decimal(profit["matecoin_price"]))
            else:
                matecoin_account += (decimal.Decimal(profit["bought"])
                                     - decimal.Decimal(profit["sold"]))
                earned_money += (decimal.Decimal(profit["sold"])
                                 * decimal.Decimal(profit["matecoin_price"]))
                earned_money -= (decimal.Decimal(profit["bought"])
                                 * decimal.Decimal(profit["matecoin_price"]))

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file2:
        json.dump(result, file2, indent=2)
