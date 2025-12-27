import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        date_about_bargain = json.load(f)
    earned_money = 0
    matecoin_account = 0
    for date in date_about_bargain:
        if date["bought"] is None:
            date["bought"] = 0
        if date["sold"] is None:
            date["sold"] = 0
        diff = decimal.Decimal(date["bought"]) - decimal.Decimal(date["sold"])
        earned_money += decimal.Decimal(date["matecoin_price"]) * diff
        matecoin_account += diff
    profit = {
        "earned_money": str(- earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
