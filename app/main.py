import json
import decimal


def calculate_profit(file_name):
    with open(file_name, "r") as f:
        trade_data = json.load(f)
        earned = decimal.Decimal("0")
        spent = decimal.Decimal("0")
        bought_coins = decimal.Decimal("0")
        sold_coins = decimal.Decimal("0")
        for day in trade_data:
            try:
                sold = decimal.Decimal(day["sold"])
            except TypeError:
                sold = decimal.Decimal("0")
            sold_coins += sold
            matecoin_price = decimal.Decimal(day["matecoin_price"])
            earned += sold * matecoin_price
            try:
                bought = decimal.Decimal(day["bought"])
            except TypeError:
                bought = decimal.Decimal("0")
            bought_coins += bought
            spent += bought * matecoin_price
        earned_money = earned - spent
        matecoin_account = bought_coins - sold_coins
        result = {"earned_money": str(earned_money),
                  "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)