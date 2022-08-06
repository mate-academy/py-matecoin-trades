import json
import decimal


def calculate_profit(*args):

    with open("trades.json", "r") as f:
        trades_data = json.load(f)
    sold_currency = 0
    bought_currency = 0
    bought = 0
    sold = 0
    if trades_data is []:
        return None
    for trade in trades_data:

        bought_currency += decimal.Decimal(
            trade["bought"]) * decimal.Decimal(trade["matecoin_price"])
        sold_currency += decimal.Decimal(
            trade["sold"]) * decimal.Decimal(trade["matecoin_price"])
        bought += decimal.Decimal(trade["bought"])
        sold = decimal.Decimal(trade["sold"])

    final_data = {
        "earned_money": decimal.Decimal(bought_currency - sold_currency),
        "matecoin_account": decimal.Decimal(bought - sold)}
    final_data = {}
    with open("profit.json") as f:
        json.dump(final_data, f)
