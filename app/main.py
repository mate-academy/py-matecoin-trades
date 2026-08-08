import json
from decimal import Decimal, getcontext


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as trades_file:
        list_of_json_data = json.load(trades_file)

    getcontext().prec = 10

    total_earned = Decimal("0.0")
    matecoin_account = Decimal("0.0")
    spent = Decimal("0.0")
    earned_money = Decimal("0.0")

    for data in list_of_json_data:
        bought = Decimal(data.get("bought", "0.0") or "0.0")
        sold = Decimal(data.get("sold", "0.0") or "0.0")
        matecoin_price = Decimal(data["matecoin_price"])

        if bought > 0 and sold > 0:
            bought_cost = bought * matecoin_price
            sold_earnings = sold * matecoin_price

            if bought >= sold:
                matecoin_account += (bought - sold)
                spent += bought_cost
                total_earned += sold_earnings
            else:
                matecoin_account -= (sold - bought)
                spent += bought_cost
                total_earned += sold_earnings
        elif bought > 0:
            spent += bought * matecoin_price
            matecoin_account += bought
        elif sold > 0:
            earned = sold * matecoin_price
            total_earned += earned
            matecoin_account -= sold

    earned_money = total_earned - spent

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit_data, profit_file, indent=2)
