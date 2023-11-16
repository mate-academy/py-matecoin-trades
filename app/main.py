from decimal import Decimal
import json


def calculate_profit(name: str) -> None:
    bought_in_dollars = Decimal("0")
    sold_in_dollars = Decimal("0")
    matecoin_account = Decimal("0")

    with open(f"{name}", "r") as trades:
        trades_data = json.load(trades)

        for trade in trades_data:
            bought_coin = trade["bought"]
            sold_coin = trade["sold"]
            matecoin_price = trade["matecoin_price"]

            if bought_coin:
                bought_in_dollars += (
                    Decimal(bought_coin)
                    * Decimal(matecoin_price)
                )
            if sold_coin:
                sold_in_dollars += (
                    Decimal(sold_coin)
                    * Decimal(matecoin_price)
                )

            if bought_coin and sold_coin:
                matecoin_account += Decimal(bought_coin) - Decimal(sold_coin)

        earned_money = bought_in_dollars - sold_in_dollars

    data_profit = {
        "earned_money": f"{-earned_money}",
        "matecoin_account": f"{matecoin_account}"
    }

    with open("profit.json", "w") as file:
        json.dump(data_profit, file, indent=2)
