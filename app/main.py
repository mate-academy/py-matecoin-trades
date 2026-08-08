import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as trade_file:
        trades = json.load(trade_file)

    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = decimal.Decimal(trade.get("matecoin_price"))

        if bought is not None:
            bought = decimal.Decimal(bought)
            earned_money -= bought * matecoin_price
            matecoin_account += bought

        if sold is not None:
            sold = decimal.Decimal(sold)
            earned_money += sold * matecoin_price
            matecoin_account -= sold

        res_dict = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as profit_file:
            json.dump(res_dict, profit_file, indent=2)
