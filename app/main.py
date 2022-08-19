import json
from decimal import Decimal


def calculate_profit(name: str):

    with open(name) as f:
        crypto_data = json.load(f)

    profit = 0
    matecoin_account = 0

    for key in crypto_data:
        if key["bought"] is not None:
            matecoin_account += Decimal(key["bought"])
            profit -= Decimal(key["bought"]) * Decimal(key["matecoin_price"])
        print(crypto_data)
        if key["sold"] is not None:
            matecoin_account -= Decimal(key["sold"])
            profit += Decimal(key["sold"]) * Decimal(key["matecoin_price"])

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
