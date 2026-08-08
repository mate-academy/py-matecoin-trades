import json
import decimal


def calculate_profit(name_of_file: str) -> None:
    money = 0
    matecoins = 0
    with open(name_of_file) as f:
        trades = json.load(f)
    for dct in trades:
        if dct["bought"] is None and dct["sold"] is not None:
            money += (decimal.Decimal(dct["sold"])
                      * decimal.Decimal(dct["matecoin_price"]))
            matecoins -= decimal.Decimal(dct["sold"])
        elif dct["sold"] is None and dct["bought"] is not None:
            money -= (decimal.Decimal(dct["bought"])
                      * decimal.Decimal(dct["matecoin_price"]))
            matecoins += decimal.Decimal(dct["bought"])
        elif dct["sold"] is not None and dct["bought"] is not None:
            money += (decimal.Decimal(dct["sold"])
                      * decimal.Decimal(dct["matecoin_price"]))
            matecoins -= decimal.Decimal(dct["sold"])
            money -= (decimal.Decimal(dct["bought"])
                      * decimal.Decimal(dct["matecoin_price"]))
            matecoins += decimal.Decimal(dct["bought"])
    with open("profit.json", "w") as new_file:
        json.dump(
            {
                "earned_money": str(money),
                "matecoin_account": str(matecoins)
            }, new_file, indent=2)
