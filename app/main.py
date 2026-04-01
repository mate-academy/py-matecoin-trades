import json
import decimal


def calculate_profit(trades: None) -> None:
    with open(trades, "r") as file:
        trades_list = json.load(file)
        earned_money = decimal.Decimal("0")
        matecoin_account = decimal.Decimal("0")

        for trade in trades_list:
            price = decimal.Decimal(trade["matecoin_price"])

            if trade["bought"] is not None:
                amount_bought = decimal.Decimal(trade["bought"])
                matecoin_account += amount_bought
                earned_money -= amount_bought * price

            if trade["sold"] is not None:
                amount_sold = decimal.Decimal(trade["sold"])
                matecoin_account -= amount_sold
                earned_money += amount_sold * price

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as outfile:
            json.dump(result, outfile, indent=2)
