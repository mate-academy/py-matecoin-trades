import json
import decimal


def calculate_profit(json_file: str) -> None:
    with open(json_file, "r") as trades_file:
        trades = json.load(trades_file)

    matecoin_account = 0
    earned_money = 0

    for trade in trades:
        matecoin_price = decimal.Decimal(trade["matecoin_price"])
        trade_amount = 0

        if trade["bought"] and trade["sold"]:
            trade_amount = (decimal.Decimal(trade["bought"])
                            - decimal.Decimal(trade["sold"]))
        elif trade["bought"]:
            trade_amount = decimal.Decimal(trade["bought"])
        elif trade["sold"]:
            trade_amount = -decimal.Decimal(trade["sold"])

        matecoin_account += trade_amount
        earned_money -= matecoin_price * trade_amount

    profit_calculations = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit_calculations, profit_file, indent=2)
