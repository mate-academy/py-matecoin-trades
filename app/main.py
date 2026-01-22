import json
import decimal


def calculate_profit(filename):

    with open(filename, "r") as f:
        trades_data = json.load(f)
    sold_currency = 0
    bought_currency = 0
    bought = 0
    sold = 0
    if trades_data is []:
        return None
    for trade in trades_data:
        if trade["bought"] is not None:
            bought_currency += decimal.Decimal(
                trade["bought"]) * decimal.Decimal(trade["matecoin_price"])
            bought += decimal.Decimal(trade["bought"])
        if trade["sold"] is not None:
            sold_currency += decimal.Decimal(
                trade["sold"]) * decimal.Decimal(trade["matecoin_price"])
            sold += decimal.Decimal(trade["sold"])

    final_data = {
        "earned_money": str(sold_currency - bought_currency),
        "matecoin_account": str(bought - sold)}

    with open("profit.json", "w") as f:
        json.dump(final_data, f, indent=2)
