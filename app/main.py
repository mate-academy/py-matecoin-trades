import json
import decimal


def coin_exchange(coin: decimal, currency: decimal) -> decimal:
    return decimal.Decimal(str(coin)) * decimal.Decimal(str(currency))


def calculate_profit(filename: str) -> None:
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    with open(filename, "r") as file, open("profit.json", "a") as profit:
        trades = json.load(file)

        for trade in trades:
            if trade["bought"]:
                earned_money -= coin_exchange(
                    trade["bought"],
                    trade["matecoin_price"]
                )
                matecoin_account += decimal.Decimal(str(trade["bought"]))
            if trade["sold"]:
                earned_money += coin_exchange(
                    trade["sold"],
                    trade["matecoin_price"]
                )
                matecoin_account -= decimal.Decimal(str(trade["sold"]))

        profit_info = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        json.dump(profit_info, profit, indent=2)
