import json
import decimal


def calculate_profit(trades: json) -> None:
    with open(trades) as file:
        trades_dict = json.load(file)

    sum_bought_coin = decimal.Decimal("0.0")
    sum_sold_coin = decimal.Decimal("0.0")
    all_bought_coin = decimal.Decimal("0.0")
    all_sold_coin = decimal.Decimal("0.0")
    for items in trades_dict:
        if items["bought"] is not None:
            sum_bought_coin += decimal.Decimal(
                items["bought"]) * decimal.Decimal(items["matecoin_price"])
            all_bought_coin += decimal.Decimal(items["bought"])
        if items["sold"] is not None:
            sum_sold_coin += decimal.Decimal(
                items["sold"]) * decimal.Decimal(items["matecoin_price"])
            all_sold_coin += decimal.Decimal(items["sold"])

    profit_dict = {
        "earned_money": str(sum_sold_coin - sum_bought_coin),
        "matecoin_account": str(all_bought_coin - all_sold_coin)
    }

    with open("profit.json", "w") as profit:
        json.dump(profit_dict, profit, indent=2)
