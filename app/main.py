import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        data = json.load(f)
    matecoin_account = decimal.Decimal("0.0")
    earned_money = decimal.Decimal("0.0")
    for transaction in data:
        if transaction["bought"] is not None:
            matecoin_account += decimal.Decimal(transaction["bought"])
            earned_money -= (decimal.Decimal(transaction["matecoin_price"])
                             * decimal.Decimal(transaction["bought"]))
        if transaction["sold"] is not None:
            matecoin_account -= decimal.Decimal(transaction["sold"])
            earned_money += (decimal.Decimal(transaction["matecoin_price"])
                             * decimal.Decimal(transaction["sold"]))
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
