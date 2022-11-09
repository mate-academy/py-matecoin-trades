import json
import decimal


def calculate_profit(file_js: str) -> None:
    with open(file_js, "r") as f_trades, open("profit.json", "w") as f_profit:
        earned_money = decimal.Decimal("0")
        matecoin_account = decimal.Decimal("0")
        trades_list = json.load(f_trades)
        for trade in trades_list:
            matecoin_price_dc = decimal.Decimal(trade["matecoin_price"])
            if trade["bought"]:
                bought_dc = decimal.Decimal(trade["bought"])
                matecoin_account += bought_dc
                earned_money -= bought_dc * matecoin_price_dc
            if trade["sold"]:
                sold_dc = decimal.Decimal(trade["sold"])
                matecoin_account -= sold_dc
                earned_money += sold_dc * matecoin_price_dc
        json_dump = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        json.dump(json_dump, f_profit, indent=2)
