import json
import decimal


def calculate_profit(file_name: str = "trades.json") -> None:
    with open(file_name, "r") as file:
        trade_data = json.load(file)

    earned_money = decimal.Decimal("0")
    matecoin_balance = decimal.Decimal("0")
    for order in trade_data:
        bought = order.get("bought")
        sold = order.get("sold")
        matecoin_price = order.get("matecoin_price")
        if bought:
            earned_money -= (
                decimal.Decimal(bought) * decimal.Decimal(matecoin_price)
            )
            matecoin_balance -= decimal.Decimal(bought)
        if sold:
            earned_money += (
                decimal.Decimal(sold) * decimal.Decimal(matecoin_price)
            )
            matecoin_balance += decimal.Decimal(sold)

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_balance * -1)
    }

    with open("./profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
