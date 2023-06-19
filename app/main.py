import decimal
import json


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as trades:
        trades_dict = json.load(trades)
    earned_money, matecoin_account = decimal.Decimal("0"), decimal.Decimal("0")
    for trade in trades_dict:
        price = decimal.Decimal(trade["matecoin_price"])
        if trade["bought"]:
            matecoin_account += decimal.Decimal(trade["bought"])
            earned_money -= decimal.Decimal(trade["bought"]) * price
        if trade["sold"]:
            matecoin_account -= decimal.Decimal(trade["sold"])
            earned_money += decimal.Decimal(trade["sold"]) * price
    with open("profit.json", "w") as profit:
        json.dump({"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)},
                  profit,
                  indent=2)
