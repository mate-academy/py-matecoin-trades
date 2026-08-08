import json
import decimal


def calculate_profit(input_file: str) -> None:
    with open(f"{input_file}", "r") as f:
        coin_dict = json.load(f)
    earned_money = 0
    matecoin_account = 0
    for key in coin_dict:
        if key["bought"] is not None:
            earned_money -= (decimal.Decimal(key["bought"])
                             * decimal.Decimal(key["matecoin_price"]))
            matecoin_account += decimal.Decimal(key["bought"])
        if key["sold"] is not None:
            earned_money += (decimal.Decimal(key["sold"])
                             * decimal.Decimal(key["matecoin_price"]))
            matecoin_account -= decimal.Decimal(key["sold"])
    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as p:
        json.dump(profit_dict, p, indent=2)
