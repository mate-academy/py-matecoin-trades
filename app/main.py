import json
import decimal


def calculate_profit(file_trades: json) -> None:
    with open(file_trades) as f:
        trades = json.load(f)
    purchase_costs = decimal.Decimal("0")
    sales_revenue = decimal.Decimal("0")
    bought_coins = decimal.Decimal("0")
    sold_coins = decimal.Decimal("0")
    for one_transaction in trades:
        num_matecoin_price_dec = (
            decimal.Decimal(one_transaction["matecoin_price"])
        )
        if one_transaction["bought"]:
            num_bought_dec = decimal.Decimal(one_transaction["bought"])
            bought_coins += num_bought_dec
            purchase_costs += num_matecoin_price_dec * num_bought_dec
        if one_transaction["sold"]:
            num_sold_dec = decimal.Decimal(one_transaction["sold"])
            sold_coins += num_sold_dec
            sales_revenue += num_matecoin_price_dec * num_sold_dec
    profit = {}
    profit["earned_money"] = str(sales_revenue - purchase_costs)
    profit["matecoin_account"] = str(bought_coins - sold_coins)
    with open("profit.json", "w") as new_file:
        json.dump(profit, new_file, indent=2)
