import json
import decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as f:
        trades_data = json.load(f)

        profit = decimal.Decimal(0.0)
        matecoins = decimal.Decimal(0.0)

        for operation in trades_data:
            matecoin_price = decimal.Decimal(operation["matecoin_price"])
            if operation["bought"] is not None:
                bought = decimal.Decimal(operation["bought"])
                matecoins += bought
                profit -= bought * matecoin_price

            if operation["sold"] is not None:
                sold = decimal.Decimal(operation["sold"])
                matecoins -= sold
                profit += sold * matecoin_price

    res = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoins)
    }

    with open("profit.json", "w") as f:
        json.dump(res, f, indent=2)
