import json
import decimal


def calculate_profit(trades: str) -> None:
    with open(trades) as f:
        user_data = json.load(f)
    earned_money = 0
    matecoin_account = 0
    for i in user_data:
        if i["bought"] is not None:
            matecoin_account += decimal.Decimal(i["bought"])
            earned_money -= decimal.Decimal(
                i["matecoin_price"]
            ) * decimal.Decimal(i["bought"])
        if i["sold"] is not None:
            matecoin_account -= decimal.Decimal(i["sold"])
            earned_money += decimal.Decimal(
                i["matecoin_price"]
            ) * decimal.Decimal(i["sold"])

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
