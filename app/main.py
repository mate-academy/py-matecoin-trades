import json
import decimal


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as data:
        trades = json.load(data)

    res = {"earned_money": decimal.Decimal("0"),
           "matecoin_account": decimal.Decimal("0")}

    for transaction in trades:
        price = decimal.Decimal(transaction["matecoin_price"])

        if transaction["bought"]:
            bought = decimal.Decimal(transaction["bought"])
            res["earned_money"] -= bought * price
            res["matecoin_account"] += bought

        if transaction["sold"]:
            sold = decimal.Decimal(transaction["sold"])
            res["earned_money"] += sold * price
            res["matecoin_account"] -= sold

    res["earned_money"] = str(res["earned_money"])
    res["matecoin_account"] = str(res["matecoin_account"])

    with open("profit.json", "w") as data:
        json.dump(res, data, indent=2)
