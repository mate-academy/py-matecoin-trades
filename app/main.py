from decimal import Decimal
import json


def calculate_profit(name: str) -> None:
    bought_in_dollars = Decimal("0")
    sold_in_dollars = Decimal("0")
    matecoin_account = Decimal("0")

    with open(name, "r") as trades_file:
        trades_data = json.load(trades_file)

        for trade in trades_data:
            bought_coin = trade.get("bought", 0)
            sold_coin = trade.get("sold", 0)
            matecoin_price = trade.get("matecoin_price", 0)

            if bought_coin:
                bought_in_dollars += (
                    Decimal(bought_coin)
                    * Decimal(matecoin_price)
                )
                matecoin_account += Decimal(bought_coin)
            if sold_coin:
                sold_in_dollars += Decimal(sold_coin) * Decimal(matecoin_price)
                matecoin_account -= Decimal(sold_coin)

    earned_money = bought_in_dollars - sold_in_dollars

    data_profit = {
        "earned_money": f"{-earned_money}",
        "matecoin_account": f"{matecoin_account}"
    }

    with open("profit.json", "w") as file:
        json.dump(data_profit, file, indent=2)
