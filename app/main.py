import json
import decimal


def calculate_profit(file_name):
    with open(file_name) as f:
        trade_info = json.load(f)
    matecoin_account = 0
    earned_money = 0
    for deal in trade_info:
        if isinstance(deal["bought"], str):
            matecoin_account += decimal.Decimal(deal["bought"])
            earned_money -= decimal.Decimal(
                deal["bought"]) * decimal.Decimal(deal["matecoin_price"])
        if isinstance(deal["sold"], str):
            matecoin_account -= decimal.Decimal(deal["sold"])
            earned_money += decimal.Decimal(
                deal["sold"]) * decimal.Decimal(deal["matecoin_price"])
    result_info = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as f:
        json.dump(result_info, f, indent=2)
