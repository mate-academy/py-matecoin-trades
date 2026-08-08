import json
import decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trade_list = json.load(file)
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")
    for trade in trade_list:
        price = decimal.Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought_amount = decimal.Decimal(trade["bought"])
            total_spent = bought_amount * price
            matecoin_account += bought_amount
            earned_money -= total_spent

        if trade["sold"] is not None:
            sold_amount = decimal.Decimal(trade["sold"])
            total_received = sold_amount * price
            matecoin_account -= sold_amount
            earned_money += total_received

    result_trading = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result_trading, f, indent=2)
