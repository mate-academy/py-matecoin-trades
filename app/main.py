import json
from decimal import Decimal


def calculate_profit(trades_path: str = "trades.json") -> None:
    try:
        with open(trades_path, "r") as file:
            trades = json.load(file)

            earned_money = Decimal("0.0")
            matecoin_account = Decimal("0.0")

            for trade in trades:
                bought, sold, matecoin_price = trade.values()

                matecoin_price_d = Decimal(str(matecoin_price))

                if bought is not None:
                    bought_d = Decimal(str(bought))

                    earned_money = earned_money - (bought_d * matecoin_price_d)
                    matecoin_account = matecoin_account + bought_d

                if sold is not None:
                    sold_d = Decimal(str(sold))
                    earned_money = earned_money + (sold_d * matecoin_price_d)
                    matecoin_account = matecoin_account - sold_d

            with open("profit.json", "w") as profit_file:
                profit_obj = {
                    "earned_money": str(earned_money),
                    "matecoin_account": str(matecoin_account)
                }
                json.dump(profit_obj, profit_file, indent=2)

    except (FileExistsError, FileNotFoundError) as e:
        print("Some error occurred: ", e)


calculate_profit()
