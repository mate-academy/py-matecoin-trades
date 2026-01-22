import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")
    for trade in trades:
        if trade.get("bought"):
            bought = (
                decimal.Decimal(trade["bought"])
                * decimal.Decimal(trade["matecoin_price"])
            )
            earned_money -= bought
            matecoin_account += decimal.Decimal(trade["bought"])
        if trade.get("sold"):
            sold = (
                decimal.Decimal(trade["sold"])
                * decimal.Decimal(trade["matecoin_price"])
            )
            earned_money += sold
            matecoin_account -= decimal.Decimal(trade["sold"])
    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
