import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trade_data = json.load(f)
        earned_money = 0
        matecoin_account = 0
        for trade_operation in trade_data:
            price = decimal.Decimal(trade_operation["matecoin_price"])
            if trade_operation["bought"] is not None:
                bought = decimal.Decimal(trade_operation["bought"])
                earned_money -= bought * price
                matecoin_account += decimal.Decimal(trade_operation["bought"])
            if trade_operation["sold"] is not None:
                sold = decimal.Decimal(trade_operation["sold"])
                earned_money += sold * price
                matecoin_account -= decimal.Decimal(trade_operation["sold"])
    earned_money = str(earned_money)
    matecoin_account = str(matecoin_account)
    result = {
        "earned_money": earned_money,
        "matecoin_account": matecoin_account
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
