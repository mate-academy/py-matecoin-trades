import json
import decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as trades:
        trades_data = json.load(trades)
    bought_amount = 0
    sold_amount = 0
    matecoin_account = 0
    for trade in trades_data:
        if trade["bought"] is not None and trade["sold"] is not None:
            bought_amount += decimal.Decimal(trade["bought"]) *\
                decimal.Decimal(trade["matecoin_price"])
            sold_amount += decimal.Decimal(trade["sold"]) * \
                decimal.Decimal(trade["matecoin_price"])
            matecoin_account += decimal.Decimal(trade["bought"])
            matecoin_account -= decimal.Decimal(trade["sold"])
        elif trade["bought"] is not None:
            bought_amount += decimal.Decimal(trade["bought"]) * \
                decimal.Decimal(trade["matecoin_price"])
            matecoin_account += decimal.Decimal(trade["bought"])
        elif trade["sold"] is not None:
            sold_amount += decimal.Decimal(trade["sold"]) * \
                decimal.Decimal(trade["matecoin_price"])
            matecoin_account -= decimal.Decimal(trade["sold"])
    profit = {"earned_money": str(sold_amount - bought_amount),
              "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as profit_json:
        json.dump(profit, profit_json, indent=2)
