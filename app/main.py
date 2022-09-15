import decimal
import json


def calculate_profit(trades):
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")
    profit_data = {}
    with open(trades) as t:
        trades_data = json.load(t)
    for day in trades_data:
        # buying
        if day["sold"] is None:
            earned_money -= decimal.Decimal(
                day["bought"]) * decimal.Decimal(day["matecoin_price"])
            matecoin_account += decimal.Decimal(day["bought"])
        # sale
        elif day["bought"] is None:
            earned_money += decimal.Decimal(
                day["sold"]) * decimal.Decimal(day["matecoin_price"])
            matecoin_account -= decimal.Decimal(day["sold"])
        # sale & buying
        else:
            earned_money += (decimal.Decimal(
                day["sold"]) - decimal.Decimal(
                day["bought"])) * decimal.Decimal(day["matecoin_price"])
            matecoin_account += decimal.Decimal(
                day["bought"]) - decimal.Decimal(day["sold"])
    profit_data["earned_money"] = str(earned_money)
    profit_data["matecoin_account"] = str(matecoin_account)
    with open("profit.json", "w") as profit:
        json.dump(profit_data, profit, indent=2)
