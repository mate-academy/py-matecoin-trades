import json
from decimal import Decimal
from json import JSONDecodeError


def calculate_profit(trades_file: int) -> None:
    try:
        with open(trades_file, "r") as file:
            trades_data = json.load(file, parse_int=Decimal)

        earned_money = Decimal("0.0")
        matecoin_account = Decimal("0.0")

        for trade in trades_data:
            bought = trade.get("bought")
            sold = trade.get("sold")
            price = Decimal(trade.get("matecoin_price", "0"))

            if bought is not None:
                bought = Decimal(bought)
                earned_money -= bought * price
                matecoin_account += bought

            if sold is not None:
                sold = Decimal(sold)
                earned_money += sold * price
                matecoin_account -= sold

        result = {
            "earned_money": str(earned_money.quantize(Decimal("0.0000001"))),
            "matecoin_account": str(
                matecoin_account.quantize(Decimal("0.00001"))
            )
        }

        with open("profit.json", "w") as profit:
            json.dump(result, profit, indent=2, separators=(",", ": "))

    except FileNotFoundError:
        print(f"file {trades_file} not fount")
    except JSONDecodeError:
        print(f"incorrect format {profit}")
    except Exception as e:
        print(f"unexpected error {e}")
