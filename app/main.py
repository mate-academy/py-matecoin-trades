import decimal
import json


def calculate_profit(file_name: str) -> None:
    with (
        open(file_name, "r") as file_in,
        open("profit.json", "w") as file_out
    ):
        trades = json.load(file_in)
        earned_money = decimal.Decimal("0")
        matecoin_account = decimal.Decimal("0")
        for trade in trades:
            current_coin_price = decimal.Decimal(trade.get("matecoin_price"))
            if purchased_coins := trade.get("bought"):
                matecoin_account += decimal.Decimal(purchased_coins)
                earned_money -= (decimal.Decimal(purchased_coins)
                                 * current_coin_price)
            if sold_coins := trade.get("sold"):
                matecoin_account -= decimal.Decimal(sold_coins)
                earned_money += (decimal.Decimal(sold_coins)
                                 * current_coin_price)

        data_for_profit_file = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }

        json.dump(data_for_profit_file, file_out, indent=2)
