import json
import decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file) as f:
        trades_data = json.load(f)
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")
    for trade in trades_data:
        matecoin_price = decimal.Decimal(trade["matecoin_price"])
        if trade["sold"]:
            sold = decimal.Decimal(trade["sold"])
            earned_money += matecoin_price * sold
            matecoin_account -= sold
        if trade["bought"]:
            bought = decimal.Decimal(trade["bought"])
            earned_money -= matecoin_price * bought
            matecoin_account += bought
    profit_data = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as f:
        json.dump(profit_data, f, indent=2)
