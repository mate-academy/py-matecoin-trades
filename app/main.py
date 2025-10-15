import json
import decimal


def calculate_profit(file_name: str) -> None:
    with (open(file_name, "rb") as python_file):
        trades = json.load(python_file)
        profit_json = {}
        matecoin_account = 0
        for trade in trades:
            matecoin_price = decimal.Decimal(trade.get("matecoin_price", 0))
            if trade["bought"]:
                bought = decimal.Decimal(trade.get("bought", 0))
                outcome = bought * matecoin_price
            else:
                outcome = decimal.Decimal(0)
                bought = 0
            if trade["sold"]:
                income = decimal.Decimal(trade.get("sold", 0)) * matecoin_price
                sold = decimal.Decimal(trade.get("sold", 0))
            else:
                income = decimal.Decimal(0)
                sold = 0
            profit_json["earned_money"] = (

                profit_json.get("earned_money", 0)
                + income
                - outcome
            )
            matecoin_account += bought - sold
        profit_json["earned_money"] = str(profit_json["earned_money"])
        profit_json["matecoin_account"] = str(matecoin_account)
    with open("profit.json", "w") as file_json:
        json.dump(profit_json, file_json, indent=2)
