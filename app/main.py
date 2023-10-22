from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        trade_deals = json.load(file)

        earned_money, matecoin_account = 0, 0

        for deal in trade_deals:
            bought, sold = deal.get("bought"), deal.get("sold")

            if deal.get("bought"):
                earned_money -= (
                    Decimal(deal.get("matecoin_price")) * Decimal(bought)
                )
                matecoin_account += Decimal(bought)

            if deal.get("sold"):
                earned_money += (
                    Decimal(deal.get("matecoin_price")) * Decimal(sold)
                )
                matecoin_account -= Decimal(sold)

        trade_result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

    with open("profit.json", "w") as result_file:
        json.dump(trade_result, result_file, indent=2)


calculate_profit("app/trades.json")
