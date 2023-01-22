import decimal
import json


def calculate_profit(trade_file: str) -> None:
    with open(trade_file, "r") as trades_info_json:
        trades_data_list = json.load(trades_info_json)

    earned_money = decimal.Decimal("0.0")
    matecoin_account = decimal.Decimal("0.0")

    for each_trade in trades_data_list:
        if each_trade["bought"] is not None:
            earned_money -= decimal.Decimal(each_trade["bought"]) *\
                decimal.Decimal(each_trade["matecoin_price"])
            matecoin_account += decimal.Decimal(each_trade["bought"])
        if each_trade["sold"] is not None:
            earned_money += decimal.Decimal(each_trade["sold"]) *\
                decimal.Decimal(each_trade["matecoin_price"])
            matecoin_account -= decimal.Decimal(each_trade["sold"])

    result_trade = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as profit_info:
        json.dump(result_trade, profit_info, indent=2)
